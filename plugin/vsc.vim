" Vim filetype plugin to start the Vimscript syntax checker from inside Vim
" Last Change: 2013-10-27
" Maintainer: Daniel Schemala <istjanichtzufassen@gmail.com>

if exists("g:loaded_vsc")
	finish
endif
let g:loaded_typecorr = 1

let g:vsc_path = expand('<sfile>:p:h') . '/vsc.py'
command! VSC :call vsc#vsc#check(expand("%:p"))
