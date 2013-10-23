
let g:vsc_path = expand('<sfile>:p:h') . '/vsc.py'
command! VSC :call vsc#vsc#check(expand("%:p"))
