
fu! vsc#vsc#check(filename)
    let old_errorformat = &errorformat
    let old_makeprg = &makeprg
	let &makeprg = 'python ' . g:vsc_path . ' %'
	let &errorformat = '%f:%l:%trror: %m,%f:%l:%tarning: %m'
	silent make
    redraw!
    cwindow
    let &errorformat = old_errorformat
    let &makeprg = old_makeprg
endf

