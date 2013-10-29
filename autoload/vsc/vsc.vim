
fu! vsc#vsc#check(...)
    if a:0 == 0
        let inputfiles = [expand('%:p')]
    else
        let inputfiles = a:000
    endif
    let old_errorformat = &errorformat
    let old_makeprg = &makeprg
	let &makeprg = 'python ' . g:vsc_path . ' ' . join(inputfiles)
	let &errorformat = '%f:%l:%trror: %m,%f:%l:%tarning: %m'
	silent make
    redraw!
    cwindow
    let &errorformat = old_errorformat
    let &makeprg = old_makeprg
endf

