#!/usr/bin/env python3
"""Term ledger: the names a paper gives to things, built from the author's own text.

Two calls.

  python scripts/term_ledger.py <paper files…> [--cited <files…>] --out ledger.json
      Statistical candidates from the author's text (.tex, .md, .txt; .pdf when PyMuPDF is installed).
      Four signals, any one admits a candidate: (a) marked or defined at first use (\\emph, \\textit,
      \\textbf, ``quotes'', "we call / refer to … as / termed"); (b) used in a heading, \\paragraph label
      or caption; (c) shared with at least two of the cited files; (d) recurring (>= 3 times) and specific
      against the award pool (references/pool_noun_stats.json). Writes ledger.json and ledger.md.

  python scripts/term_ledger.py --verify names.json ledger.json
      names.json is the list a model wrote after reading the text ([{"term", "kind", "names",
      "sentence"}…]); only terms that occur verbatim in the author's text are kept, counted and merged
      into ledger.json. Nothing a model wrote enters the ledger without this check.

The ledger is the author's vocabulary: used verbatim, one name per thing, no coined multiword labels.
The author prunes it once. check_tex.py --ledger ledger.json reports unused names and possible coinages.
"""
import argparse, collections, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('files', nargs='*')
ap.add_argument('--cited', nargs='*', default=[])
ap.add_argument('--out', default='ledger.json')
ap.add_argument('--verify', nargs=2, metavar=('NAMES_JSON', 'LEDGER_JSON'))
ap.add_argument('--pool-stats', default=os.path.join(HERE, '..', 'references', 'pool_noun_stats.json'))
args = ap.parse_args()

GENERIC_HEAD = {'model', 'models', 'method', 'methods', 'approach', 'result', 'results', 'performance', 'work', 'paper', 'task', 'tasks',
                'data', 'number', 'set', 'case', 'cases', 'example', 'examples', 'way', 'ways', 'part', 'parts', 'time', 'problem', 'problems',
                'question', 'questions', 'figure', 'table', 'section', 'appendix', 'experiment', 'experiments', 'setting', 'settings', 'detail',
                'details', 'fact', 'point', 'type', 'types', 'kind', 'thing', 'things', 'process', 'step', 'steps', 'order', 'terms', 'term'}


def read(path):
    if path.lower().endswith('.pdf'):
        try:
            import fitz
            return '\n'.join(p.get_text() for p in fitz.open(path))
        except Exception as e:
            print(f'skip {path}: {e}', file=sys.stderr); return ''
    return open(path, errors='ignore').read()


def strip(t):
    t = t.replace('\\$', ' DOLLAR ')
    t = re.sub(r'\\begin\{(table|figure|wraptable|wrapfigure|algorithm|algorithmic|equation|align|tikzpicture)\*?\}.*?\\end\{\1\*?\}', ' ', t, flags=re.S)
    t = re.sub(r'\\(cite\w*|citep|citet)\*?(\[[^\]]*\])?\{[^}]*\}', ' ', t)
    t = re.sub(r'\\(ref|cref|Cref|eqref|autoref|label)\*?\{[^}]*\}', ' ', t)
    t = re.sub(r'\$\$.*?\$\$', ' X ', t, flags=re.S); t = re.sub(r'\$[^$]*\$', ' X ', t)
    for _ in range(3):
        t = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?\{([^{}]*)\}', r'\2', t)
    t = re.sub(r'\\[a-zA-Z]+\*?', ' ', t); t = re.sub(r'(?<!\\)%.*', '', t)
    t = re.sub(r"``|''", '"', t); t = re.sub(r'[{}~]', ' ', t)
    return re.sub(r'\s+', ' ', t)


def exact_count(term, low):
    return len(re.findall(r'(?<![\w-])' + re.escape(term.lower()).replace(r'\ ', r'[\s-]+') + r'(?![\w-])', low))


if args.verify:
    names_p, ledger_p = args.verify
    ledger = json.load(open(ledger_p)); low = ledger['_text'].lower()
    names = json.load(open(names_p)); have = {e['term'].lower() for e in ledger['entries']}
    kept, dropped = [], []
    for n in names:
        term = re.sub(r'[*"`]', '', str(n.get('term', ''))).strip()
        c = exact_count(term, low) if term else 0
        if c == 0:
            dropped.append(term); continue
        if term.lower() in have:
            continue
        kept.append(dict(term=term, count=c, kind=n.get('kind', 'own'), names=n.get('names', ''), sentence=str(n.get('sentence', ''))[:240], source='model, verified'))
    ledger['entries'] = kept + ledger['entries']
    json.dump(ledger, open(ledger_p, 'w'), indent=1, ensure_ascii=False)
    md = ledger_p[:-5] + '.md' if ledger_p.endswith('.json') else ledger_p + '.md'
    with open(md, 'w') as fh:
        fh.write(f"# Term ledger\n\n{len(ledger['entries'])} names; the author prunes once.\n\n| term | n | kind | what it names | source sentence |\n|---|---|---|---|---|\n")
        for e in ledger['entries']:
            fh.write(f"| {e['term']} | {e['count']} | {e.get('kind', '')} | {e.get('names', '')} | {e.get('sentence', '')[:120]} |\n")
    print(f'verified {len(kept)} of {len(names)} model names; dropped (not verbatim): {dropped[:10]}{" …" if len(dropped) > 10 else ""}; ledger now {len(ledger["entries"])} entries -> {ledger_p}, {md}')
    sys.exit()

if not args.files:
    ap.error('give the paper files, or --verify names.json ledger.json')
try:
    import spacy
    nlp = spacy.load('en_core_web_sm', disable=['ner']); nlp.max_length = 3_000_000
except Exception as e:
    sys.exit(f'spaCy with en_core_web_sm is needed for the statistical candidates ({e}); the --verify call works without it')

raw = '\n'.join(read(f) for f in args.files)
body = strip(raw); low = body.lower()


def chunks(doc):
    for ch in doc.noun_chunks:
        toks = list(ch)
        while toks and (toks[0].is_stop or toks[0].pos_ in ('DET', 'PRON', 'NUM', 'PUNCT', 'CCONJ', 'ADP')):
            toks = toks[1:]
        toks = [x for x in toks if not (x.is_punct and x.text != '-') and x.text != 'X' and x.pos_ not in ('DET', 'PRON', 'PART', 'CCONJ', 'ADP', 'SCONJ')]
        if not toks or toks[-1].pos_ not in ('NOUN', 'PROPN') or len(toks) > 6:
            continue
        lem = ' '.join(x.lemma_.lower() for x in toks).replace(' - ', '-'); surf = ' '.join(x.text for x in toks).replace(' - ', '-')
        if len(lem) < 4 or (len(toks) == 1 and lem in GENERIC_HEAD):
            continue
        yield lem, surf, ch.sent.text


# (a) marks and definitions on the raw text
defined = collections.OrderedDict()
for m in re.finditer(r'\\(emph|textit|textbf)\{([^{}]{3,60})\}', raw):
    t = m.group(2).strip()
    if re.search(r'[a-z]', t) and len(t.split()) <= 5 and not re.search(r'\\|\$', t):
        defined.setdefault(t.lower(), set()).add('marked')
for m in re.finditer(r"``([^'`]{3,60})''|\"([^\"]{3,60})\"", raw):
    t = (m.group(1) or m.group(2) or '').strip()
    if t and len(t.split()) <= 5 and re.search(r'[a-z]', t):
        defined.setdefault(t.lower(), set()).add('quoted')
for m in re.finditer(r'(?:we (?:call|term|dub|name|refer to|denote)|termed|dubbed|henceforth|hereafter|referred to as|which we call|is called)\s+(?:this|these|it|them|the|a|an)?\s*([A-Za-z][\w\- ]{2,50}?)(?=[,.;:\s]|$)', body):
    t = m.group(1).strip(' .,;:')
    if 1 <= len(t.split()) <= 5:
        defined.setdefault(t.lower(), set()).add('defined')
# (b) headings and captions
heads = re.findall(r'\\(?:section|subsection|subsubsection|paragraph)\*?\{([^{}]+)\}', raw) + re.findall(r'(?m)^#+\s+(.+)$', raw) + re.findall(r'\\caption\{((?:[^{}]|\{[^{}]*\})*)\}', raw)
head_surface = {}; head_terms = collections.Counter()
for h in heads:
    hs = strip(h).strip(' .:')
    for l, s, _ in chunks(nlp(hs)):
        head_terms[l] += 1
    if 1 <= len(hs.split()) <= 4 and re.search(r'[a-zA-Z]', hs) and not re.match(r'(?i)(introduction|related work|conclusion|experiments?|results?|method|discussion|limitations?|appendix|setup|background|preliminaries)$', hs):
        l = ' '.join(t.lemma_.lower() for t in nlp(hs) if not t.is_punct); head_terms[l] += 1; head_surface[l] = hs
# body noun phrases
cnt = collections.Counter(); surface = collections.defaultdict(collections.Counter); sent_of = {}
for lem, surf, sent in chunks(nlp(body[:1_500_000])):
    cnt[lem] += 1; surface[lem][surf] += 1; sent_of.setdefault(lem, sent[:240])
# (c) cited files
field_cnt = collections.Counter()
for f in args.cited:
    ft = strip(read(f))
    for l in set(l for l, _, _ in chunks(nlp(ft[:600_000]))):
        field_cnt[l] += 1
# (d) specificity
pool = json.load(open(args.pool_stats)) if os.path.exists(args.pool_stats) else {}
n_pool = pool.get('__n__') or pool.get('n_papers') or 68
pool_df = pool.get('df', pool)

entries = []
for lem in set(cnt) | set(defined) | set(head_terms):
    top = surface[lem].most_common(1)[0][0].lower() if surface.get(lem) else None
    dkey = next((k for k in defined if k == lem or (top and k == top)), None)
    sig = set(defined[dkey]) if dkey else set()
    if lem in head_terms: sig.add('heading')
    if field_cnt.get(lem, 0) >= 2: sig.add(f'cited:{field_cnt[lem]}')
    df = pool_df.get(lem, 0) if isinstance(pool_df, dict) else 0
    if cnt.get(lem, 0) >= 3 and df <= 0.15 * n_pool: sig.add(f'recurring:{cnt[lem]}')
    if not sig or (cnt.get(lem, 0) == 0 and not dkey and lem not in head_surface):
        continue
    term = surface[lem].most_common(1)[0][0] if surface.get(lem) else (head_surface.get(lem) or dkey)
    entries.append(dict(term=term, count=max(cnt.get(lem, 0), exact_count(term, low)), kind='stats', signals=sorted(sig), sentence=sent_of.get(lem, ''), source='stats'))
entries.sort(key=lambda e: (-len(e['signals']), -e['count']))
json.dump(dict(files=args.files, cited=args.cited, entries=entries, _text=body), open(args.out, 'w'), indent=1, ensure_ascii=False)
md = args.out[:-5] + '.md' if args.out.endswith('.json') else args.out + '.md'
with open(md, 'w') as fh:
    fh.write(f'# Term ledger, statistical candidates\n\n{len(entries)} candidates from {len(args.files)} file(s); the author prunes once; names a model adds go through --verify.\n\n| term | n | signals | source sentence |\n|---|---|---|---|\n')
    for e in entries:
        fh.write(f"| {e['term']} | {e['count']} | {', '.join(e['signals'])} | {e['sentence'][:120]} |\n")
print(f'{len(entries)} candidates -> {args.out}, {md}; by signal: ' + ', '.join(f'{k} {v}' for k, v in collections.Counter(s.split(":")[0] for e in entries for s in e['signals']).most_common()))
