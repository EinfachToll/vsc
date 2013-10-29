" Vim filetype plugin to start the Vimscript syntax checker from inside Vim
" Last Change: 2013-10-27
" Maintainer: Daniel Schemala <istjanichtzufassen@gmail.com>

if exists("b:did_ftplugin")
	finish
endif
let b:did_ftplugin = 1

if !exists("g:vsc_path")
	let g:vsc_path = expand('<sfile>:p:h') . '/vsc.py'
endif

command! -buffer -nargs=* -complete=file VSC :call vsc#vsc#check(<f-args>)
