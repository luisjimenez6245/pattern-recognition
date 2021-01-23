for ((VAR=10000 ; VAR<11000 ; VAR++ ))
do
    echo $VAR
    python3 app.py "$VAR" > "./bitmaps/$VAR.txt"
done