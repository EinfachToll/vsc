#!/usr/bin/env python
# coding: utf-8

import sys
import re

vimcommands = {
    "set": "se",
    "function": "fu",
    "return": "retu",
    "echo": "ec",
    "echoerr": "echoe",
    "echohl": "echoh",
    "echomsg": "echom",
    "echon": "",
    "else": "el",
    "elseif": "elsei",
    "endif": "en",
    "endfor": "endfo",
    "endfunction": "endf",
    "endtry": "endt",
    "endwhile": "endw",
    "let": "",
    "unlet": "unl",
    "while": "wh",
    "for": "",
    "if": "",
    "break": "brea",
    "call": "cal",
    "catch": "cat",
    "continue": "con",
    "tabnew": "",
    "finish": "fini",
    "py3": "",
    "python3": "",
    "python": "py",
    "perl": "pe",
    "ruby": "rub",
    "rubydo": "rubyd",
    "rubyfile": "rubyf",
    "command": "com",
    "nmap": "nm",
    "autocmd": "au",
    "augroup": "aug",
    "normal": "norm",
    "execute": "exe",
    "redraw": "redr",
    "botright": "bo",
    "silent": "sil",
    "try": "",
    "finally": "fina",
    "onoremap": "ono",
    "vnoremap": "vn",
    "inoremap": "ino",
    "abclear": "abc",
    "aboveleft": "abo",
    "syntax": "sy",
    "setlocal": "setl",
    "redir": "redi",
    "doautocmd": "do",
    "highlight": "hi",
    "bdelete": "bd",
    "bunload": "bun",
    "append": "a",
    "abbreviate": "ab",
    "belowright": "bel",
    "Next": "N",
    "Print": "P",
    "X": "",
    "all": "al",
    "amenu": "am",
    "anoremenu": "an",
    "args": "ar",
    "argadd": "arga",
    "argdelete": "argd",
    "argedit": "arge",
    "argdo": "",
    "argglobal": "argg",
    "arglocal": "argl",
    "argument": "argu",
    "ascii": "as",
    "aunmenu": "aun",
    "buffer": "b",
    "bNext": "bN",
    "ball": "ba",
    "badd": "bad",
    "behave": "be",
    "bfirst": "bf",
    "blast": "bl",
    "bmodified": "bm",
    "bnext": "bn",
    "bprevious": "bp",
    "brewind": "br",
    "breakadd": "breaka",
    "breakdel": "breakd",
    "breaklist": "breakl",
    "browse": "bro",
    "bufdo": "",
    "buffers": "",
    "bwipeout": "bw",
    "change": "c",
    "cNext": "cN",
    "cNfile": "cNf",
    "cabbrev": "ca",
    "cabclear": "cabc",
    "caddbuffer": "caddb",
    "caddexpr": "cad",
    "caddfile": "caddf",
    "cbuffer": "cb",
    "cc": "",
    "cclose": "ccl",
    "cd": "",
    "center": "ce",
    "cexpr": "cex",
    "cfile": "cf",
    "cfirst": "cfir",
    "cgetbuffer": "cgetb",
    "cgetexpr": "cgete",
    "cgetfile": "cg",
    "changes": "cha",
    "chdir": "chd",
    "checkpath": "che",
    "checktime": "checkt",
    "clist": "cl",
    "clast": "cla",
    "close": "clo",
    "cmap": "cm",
    "cmapclear": "cmapc",
    "cmenu": "cme",
    "cnext": "cn",
    "cnewer": "cnew",
    "cnfile": "cnf",
    "cnoremap": "cno",
    "cnoreabbrev": "cnorea",
    "cnoremenu": "cnoreme",
    "copy": "co",
    "colder": "col",
    "colorscheme": "colo",
    "comclear": "comc",
    "compiler": "comp",
    "confirm": "conf",
    "copen": "cope",
    "cprevious": "cp",
    "cpfile": "cpf",
    "cquit": "cq",
    "crewind": "cr",
    "cscope": "cs",
    "cstag": "cst",
    "cunmap": "cu",
    "cunabbrev": "cuna",
    "cunmenu": "cunme",
    "cwindow": "cw",
    "delete": "d",
    "delmarks": "delm",
    "debug": "deb",
    "debuggreedy": "debugg",
    "delcommand": "delc",
    "delfunction": "delf",
    "diffupdate": "dif",
    "diffget": "diffg",
    "diffoff": "diffo",
    "diffpatch": "diffp",
    "diffput": "diffpu",
    "diffsplit": "diffs",
    "diffthis": "",
    "digraphs": "dig",
    "display": "di",
    "djump": "dj",
    "dlist": "dl",
    "doautoall": "doautoa",
    "drop": "dr",
    "dsearch": "ds",
    "dsplit": "dsp",
    "edit": "e",
    "earlier": "ea",
    "emenu": "em",
    "enew": "ene",
    "ex": "",
    "exit": "exi",
    "exusage": "exu",
    "file": "f",
    "files": "",
    "filetype": "filet",
    "find": "fin",
    "first": "fir",
    "fixdel": "fix",
    "fold": "fo",
    "foldclose": "foldc",
    "folddoopen": "foldd",
    "folddoclosed": "folddoc",
    "foldopen": "foldo",
    "global": "g",
    "goto": "go",
    "grep": "gr",
    "grepadd": "grepa",
    "gui": "gu",
    "gvim": "gv",
    "hardcopy": "ha",
    "help": "h",
    "helpfind": "helpf",
    "helpgrep": "helpg",
    "helptags": "helpt",
    "hide": "hid",
    "history": "his",
    "insert": "i",
    "iabbrev": "ia",
    "iabclear": "iabc",
    "ijump": "ij",
    "ilist": "il",
    "imap": "im",
    "imapclear": "imapc",
    "imenu": "ime",
    "inoreabbrev": "inorea",
    "inoremenu": "inoreme",
    "intro": "int",
    "isearch": "is",
    "isplit": "isp",
    "iunmap": "iu",
    "iunabbrev": "iuna",
    "iunmenu": "iunme",
    "join": "j",
    "jumps": "ju",
    "k": "",
    "keepalt": "keepa",
    "keepmarks": "kee",
    "keepjumps": "keepj",
    "lNext": "lN",
    "lNfile": "lNf",
    "list": "l",
    "laddexpr": "lad",
    "laddbuffer": "laddb",
    "laddfile": "laddf",
    "last": "la",
    "language": "lan",
    "later": "lat",
    "lbuffer": "lb",
    "lcd": "lc",
    "lchdir": "lch",
    "lclose": "lcl",
    "lcscope": "lcs",
    "left": "le",
    "leftabove": "lefta",
    "lexpr": "lex",
    "lfile": "lf",
    "lfirst": "lfir",
    "lgetbuffer": "lgetb",
    "lgetexpr": "lgete",
    "lgetfile": "lg",
    "lgrep": "lgr",
    "lgrepadd": "lgrepa",
    "lhelpgrep": "lh",
    "ll": "",
    "llast": "lla",
    "llist": "lli",
    "lmake": "lmak",
    "lmap": "lm",
    "lmapclear": "lmapc",
    "lnext": "lne",
    "lnewer": "lnew",
    "lnfile": "lnf",
    "lnoremap": "ln",
    "loadkeymap": "loadk",
    "loadview": "lo",
    "lockmarks": "loc",
    "lockvar": "lockv",
    "lolder": "lol",
    "lopen": "lope",
    "lprevious": "lp",
    "lpfile": "lpf",
    "lrewind": "lr",
    "ls": "",
    "ltag": "lt",
    "lunmap": "lu",
    "lua": "",
    "luado": "luad",
    "luafile": "luaf",
    "lvimgrep": "lv",
    "lvimgrepadd": "lvimgrepa",
    "lwindow": "lw",
    "move": "m",
    "mark": "ma",
    "make": "mak",
    "map": "",
    "mapclear": "mapc",
    "marks": "",
    "match": "mat",
    "menu": "me",
    "menutranslate": "menut",
    "messages": "mes",
    "mkexrc": "mk",
    "mksession": "mks",
    "mkspell": "mksp",
    "mkvimrc": "mkv",
    "mkview": "mkvie",
    "mode": "mod",
    "mzscheme": "mz",
    "mzfile": "mzf",
    "nbclose": "nbc",
    "nbkey": "nb",
    "nbsart": "nbs",
    "next": "n",
    "new": "",
    "nmapclear": "nmapc",
    "nmenu": "nme",
    "nnoremap": "nn",
    "nnoremenu": "nnoreme",
    "noautocmd": "noa",
    "noremap": "no",
    "nohlsearch": "noh",
    "noreabbrev": "norea",
    "noremenu": "noreme",
    "number": "nu",
    "nunmap": "nun",
    "nunmenu": "nunme",
    "oldfiles": "ol",
    "open": "o",
    "omap": "om",
    "omapclear": "omapc",
    "omenu": "ome",
    "only": "on",
    "onoremenu": "onoreme",
    "options": "opt",
    "ounmap": "ou",
    "ounmenu": "ounme",
    "ownsyntax": "ow",
    "pclose": "pc",
    "pedit": "ped",
    "print": "p",
    "profdel": "profd",
    "profile": "prof",
    "promptfind": "pro",
    "promptrepl": "promptr",
    "perldo": "perld",
    "pop": "po",
    "popup": "pop",
    "ppop": "pp",
    "preserve": "pre",
    "previous": "prev",
    "psearch": "ps",
    "ptag": "pt",
    "ptNext": "ptN",
    "ptfirst": "ptf",
    "ptjump": "ptj",
    "ptlast": "ptl",
    "ptnext": "ptn",
    "ptprevious": "ptp",
    "ptrewind": "ptr",
    "ptselect": "pts",
    "put": "pu",
    "pwd": "pw",
    "py3file": "py3f",
    "pyfile": "pyf",
    "quit": "q",
    "quitall": "quita",
    "qall": "qa",
    "read": "r",
    "recover": "rec",
    "redo": "red",
    "redrawstatus": "redraws",
    "registers": "reg",
    "resize": "res",
    "retab": "ret",
    "rewind": "rew",
    "right": "ri",
    "rightbelow": "rightb",
    "rundo": "rund",
    "runtime": "ru",
    "rviminfo": "rv",
    "substitute": "s",
    "sNext": "sN",
    "sandbox": "san",
    "sargument": "sa",
    "sall": "sal",
    "saveas": "sav",
    "sbuffer": "sb",
    "sbNext": "sbN",
    "sball": "sba",
    "sbfirst": "sbf",
    "sblast": "sbl",
    "sbmodified": "sbm",
    "sbnext": "sbn",
    "sbprevious": "sbp",
    "sbrewind": "sbr",
    "scriptnames": "scrip",
    "scriptencoding": "scripte",
    "scscope": "scs",
    "setfiletype": "setf",
    "setglobal": "setg",
    "sfind": "sf",
    "sfirst": "sfir",
    "shell": "sh",
    "simalt": "sim",
    "sign": "sig",
    "sleep": "sl",
    "slast": "sla",
    "smagic": "sm",
    "smap": "sma",
    "smapclear": "smapc",
    "smenu": "sme",
    "snext": "sn",
    "sniff": "sni",
    "snomagic": "sno",
    "snoremap": "snor",
    "snoremenu": "snoreme",
    "sort": "sor",
    "source": "so",
    "spelldump": "spelld",
    "spellgood": "spe",
    "spellinfo": "spelli",
    "spellrepall": "spellr",
    "spellundo": "spellu",
    "spellwrong": "spellw",
    "split": "sp",
    "sprevious": "spr",
    "srewind": "sre",
    "stop": "st",
    "stag": "sta",
    "startinsert": "star",
    "startgreplace": "startg",
    "startreplace": "startr",
    "stopinsert": "stopi",
    "stjump": "stj",
    "stselect": "sts",
    "sunhide": "sun",
    "sunmap": "sunm",
    "sunmenu": "sunme",
    "suspend": "sus",
    "sview": "sv",
    "swapname": "sw",
    "syncbind": "sync",
    "t": "",
    "tNext": "tN",
    "tabNext": "tabN",
    "tabclose": "tabc",
    "tabdo": "",
    "tabedit": "tabe",
    "tabfind": "tabf",
    "tabfirst": "tabfir",
    "tablast": "tabl",
    "tabmove": "tabm",
    "tabnext": "tabn",
    "tabonly": "tabo",
    "tabprevious": "tabp",
    "tabrewind": "tabr",
    "tabs": "",
    "tab": "",
    "tag": "ta",
    "tags": "",
    "tcl": "tc",
    "tcldo": "tcld",
    "tclfile": "tclf",
    "tearoff": "te",
    "tfirst": "tf",
    "throw": "th",
    "tjump": "tj",
    "tlast": "tl",
    "tmenu": "tm",
    "tnext": "tn",
    "topleft": "to",
    "tprevious": "tp",
    "trewind": "tr",
    "tselect": "ts",
    "tunmenu": "tu",
    "undojoin": "undoj",
    "unlockvar": "unlo",
    "unmap": "unm",
    "unmenu": "unme",
    "unsilent": "uns",
    "update": "up",
    "verbose": "verb",
    "vertical": "vert",
    "windo": "",
    "write": "w",
    "wall": "wa",
    "winsize": "wi",
    "wincmd": "winc",
    "wq": "",
    "wqall": "wqa",
    "vmap": "vm",
    "vmapclear": "vmapc",
    "vmenu": "vme",
    "vnew": "vne",
    "vnoremenu": "vnoreme",
    "vsplit": "vs",
    "vunmap": "vu",
    "vunmenu": "vunme",
    "xmapclear": "xmapc",
    "xmap": "xm",
    "xmenu": "xme",
    "xnoremap": "xn",
    "xnoremenu": "xnoreme",
    "xunmap": "xu",
    "xunmenu": "xunme",
}

unusualvimcommands = {
    "undo": "u",
    "undolist": "undol",
    "unabbreviate": "una",
    "unhide": "unh",
    "wviminfo": "wv",
    "xall": "xa",
    "~": "",
    "wundo": "wu",
    "z": "",
    "wsverb": "ws",
    "xit": "x",
    "yank": "y",
    "wnext": "wn",
    "vglobal": "v",
    "version": "ve",
    "wprevious": "wp",
    "winpos": "winp",
    "vimgrep": "vim",
    "vimgrepadd": "vimgrepa",
    "viusage": "viu",
    "view": "vie",
    "wNext": "wN",
    "visual": "vi",
    "!": "",
    "!!": "",
    "#": "",
    "&": "",
    "*": "",
    "<": "",
    "=": "",
    ">": "",
    "@": "",
    "@@": "",
}

pattern_vimcommand = re.compile(r":?\s*(?:%|(?:\d+|\.|\$)(?:[,;](?:\d+|\.|\$))?)?\s*([a-zA-Z]\w*|[~!#&*<=>@]|!!|@@)")
pattern_str_single = re.compile(r"'(''|[^'])*'")
pattern_str_double = re.compile(r'"(\\"|[^"])*"')
pattern_function_def = re.compile(r"(fu\w*)\s*!?\s*[^(]+\(([^)]*)\)")
pattern_notvimscript = re.compile(r"(py|py3|pyt|pyth|pytho|python|python3|rub|ruby|pe|per|perl|tc|tcl|lua)\s+<<\s*(\w+)$")

issues_list = []
csstack = []
unseen_function_args = []


def error(ln, string):
    issues_list.append((ln, "Error: " + string))


def warning(ln, string):
    issues_list.append((ln, "Warning: " + string))


def getnormalizedvimcommand(word):
    for longcommand in vimcommands:
        if (longcommand.startswith(word) and word.startswith(vimcommands[longcommand])):
            return longcommand
    for longcommand in unusualvimcommands:
        if (longcommand.startswith(word) and word.startswith(unusualvimcommands[longcommand])):
            return longcommand
    return None


def getfirstcommand(line):
    firstwordmatch = pattern_vimcommand.match(line)
    if not firstwordmatch:
        return ''
    command = getnormalizedvimcommand(firstwordmatch.group(1))
    return command if command else ''


def check_firstcommand(lnum, command):
    if not command:
        warning(lnum, "Line starts with an unknown command")
    elif command in unusualvimcommands:
        warning(lnum, "'" + command + "' is a rather unusual command. Are you sure this is what you want?")


def check_start_of_control_structure(lnum, command):
    if command in ["if", "for", "while", "try", "function"]:
        csstack.append(command)


def check_elseif(lnum, command):
    if command == "elseif" and csstack[-1] != "if":
        error(lnum, "Where does this 'elseif' belong to?")


def check_else(lnum, command):
    if command == "else":
        if csstack[-1] == "else":
            error(lnum, "There can be only one 'else'")
        else:
            csstack.append("else")


def check_ending_control_structure(lnum, command):
    if command not in ["endif", "endfor", "endwhile", "endtry", "endfunction"]:
        return

    if command == "endif" and csstack[-1] == "else" and csstack[-2] == "if":
        csstack.pop()
        csstack.pop()
        return
    if command == "endif" and csstack[-1] == "if":
        csstack.pop()
        return
    if command == "endfor" and csstack[-1] == "for":
        csstack.pop()
        return
    if command == "endwhile" and csstack[-1] == "while":
        csstack.pop()
        return
    if command == "endtry" and csstack[-1] == "try":
        csstack.pop()
        return
    if command == "endfunction" and csstack[-1] == "function":
        csstack.pop()
        return

    error(lnum, "Where does this '{0}' belong to?".format(command))


def check_function_args(lnum, command, line):
    if command == "function":
        function_match = pattern_function_def.match(line)
        if not function_match:
            error(lnum, "Strange function definition here")
            return
        args = [ a.strip() for a in function_match.group(2).split(",") ]
        if args == ['']:
            args = []
        unseen_function_args.append((lnum, args))
        return

    if command == "endfunction" and len(unseen_function_args) >= 1:
        (fun_def_lnum, current_unseen_args) = unseen_function_args.pop()
        if len(current_unseen_args) > 0:
            warning(fun_def_lnum, "Unused function arguments: " + ", ".join(current_unseen_args))
        return

    seen_args = re.findall(r"\ba:(\w+)", line)

    if seen_args:
        if len(unseen_function_args) == 0:
            error(lnum, "Apparently using a function argument variable outside of a function")
            return

        (fun_def_lnum, current_unseen_args) = unseen_function_args.pop()
        for seen_arg in seen_args:
            if seen_arg in current_unseen_args:
                current_unseen_args.remove(seen_arg)
            elif re.match(r'\d+', seen_arg) and '...' in current_unseen_args:
                current_unseen_args.remove('...')
        unseen_function_args.append((fun_def_lnum, current_unseen_args))


def check(lines):
    for lnum, line in lines:

        firstcommand = getfirstcommand(line)

        check_firstcommand(lnum, firstcommand)

        check_start_of_control_structure(lnum, firstcommand)

        check_elseif(lnum, firstcommand)

        check_else(lnum, firstcommand)

        check_ending_control_structure(lnum, firstcommand)

        check_function_args(lnum, firstcommand, line)

    if len(csstack) > 2:
        error(len(lines)-1, "Dangling " + ", ".join(str(i) for i in csstack[2:]))


def joinlines(lines):
    result = [lines[0]]
    for lnum, line in lines[1:]:
        if not line.startswith('\\'):
            result.append((lnum, line))
        else:
            (lastlnum, lastline) = result.pop()
            result.append((lastlnum, lastline + line[1:]))

    return result


def strip(lines):
    return [ (ln, line.strip()) for ln, line in lines ]


def startofnotvimscript(line):
    match = pattern_notvimscript.match(line)
    if match:
        return match.group(2)
    else:
        return None


def removestuff(lines):
    """
    remove the following types of lines, because they are either too boring or
    too complicated:
        - empty lines
        - comment lines
        - lines starting with #!
        - lines with just a number (to jump to a line)
        - embedded python/ruby/tcl/perl/lua code
        - autocmd, syntax, command and *map commands
    """
    result = []
    lnum = 0
    while lnum < len(lines):
        line = lines[lnum][1]

        if line == '' or line.startswith('"') or line.startswith("#!"):
            lnum += 1
            continue

        if re.match(r"\d+", line):
            lnum += 1
            continue

        firstcommand = getfirstcommand(line)
        if firstcommand in ["autocmd", "syntax", "command"] or firstcommand.endswith("map"):
            lnum += 1
            continue

        marker = startofnotvimscript(line)
        if marker:
            while not re.match(marker, lines[lnum][1]):
                lnum += 1
            lnum += 1
            continue
        result.append(lines[lnum])
        lnum += 1
    return result


def collapsestrings(lines):
    """
    delete string literals, because they are of no use for us but may
    confuse us in further steps

    We have to make sure the first occurrence of a string literal in a line is
    deleted first, otherwise it breaks at lines like "'" bla "'"
    """
    result = []
    for lnum, line in lines:
        if re.search(r"<Bar>|\\\||\|", line):
            line = re.sub(r"<Bar>|\\\||\|", "", line)
        while True:
            match_single = pattern_str_single.search(line)
            match_double = pattern_str_double.search(line)
            if match_single and not match_double:
                line = pattern_str_single.sub("", line)
            elif match_double and not match_single:
                line = pattern_str_double.sub("", line)
            elif not match_double and not match_single:
                break
            else:
                if match_single.start() < match_double.start():
                    line = pattern_str_single.sub("", line)
                else:
                    line = pattern_str_double.sub("", line)
        result.append((lnum, line))
    return result


def splitatpipe(lines):
    result = []
    for ln, line in lines:
        splitlines = re.split(r'(?<!\|)\|(?!\|)', line)
        result.extend((ln, s) for s in splitlines)
    return result


def start(filename):
    global unseen_function_args, csstack, issues_list
    with open(filename, 'r') as fil:
        filelines = fil.readlines()

    unseen_function_args = []
    csstack = ['dummy', 'dummy']
    issues_list = []

    normalizedlines = removestuff(strip(splitatpipe(collapsestrings(removestuff(joinlines(strip(enumerate(filelines))))))))
    check(normalizedlines)

    issues_list.sort()
    for ln, message in issues_list:
        print "{0}:{1}:{2}".format(filename, ln+1, message)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Give me some Vimscript files, please"
        exit()

    vsfiles = sys.argv[1:]
    for vsfile in vsfiles:
        start(vsfile)
