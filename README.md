# eval / apply
<!--![eval / apply](doc/cover2.jpg?raw=true "Eval / apply")-->
<img src="doc/cover2.jpg" alt="hi" width="500"/>

## What
Lisp interpreter in Python

## Run
`./run_job` -or- `python3 interpreter.py -f [file.lisp]`

## Docs

    lisp_data = "(define add (a b)  " +
                "   (+ a b))        " +
                "                   " +
                "(add(2,3))         "

    parse(lisp_data)

    >>> ['define','add','a','b',['+','a','b']]

    eval(parse(lisp_data))

    >>> 5
