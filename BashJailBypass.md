# Bash Jail Escape — Blacklist Bypass via Function Injection

## 🔒 Jail Script (`jail.sh`)
```bash
#!/bin/bash
PATH=$(/usr/bin/getconf PATH || /bin/kill $$)

function check_input() {
    if [[ $1 == *[bdksiSctr'?''*''/''<''>''&''(''{''0''1''2''3''4''5''6''7''8''9']* ]]
    then
        return 0
    fi
    return 1
}

while :; do
    input=""
    echo -n "Enter the input: "
    read input
    if check_input "$input"
    then
        echo -e '\033[0;31mRestricted characters has been used\033[0m'
    else
        output=`/bin/bash -c "$input" &>/dev/null`
        echo "Command executed"
    fi
done
```

## ⚔️ Initial Analysis

The script enforces a blacklist of potentially dangerous characters including:

Critical Bash characters: b, d, k, s, i, S, c, t, r, ', ?, *, /, <, >, &, (, {

All digits 0-9

This prevents obvious shell commands like: ls /home cat /flag.txt echo $PATH

As well as indirect attempts like: echo "ls /home" | base64 eval $CMD $(ls)

All these were blocked with: Restricted characters has been used


## 🧪 Documented Attempts to Escape

Below are documented failed approaches (all blocked due to restricted characters or evaluated as inert):

🔸 Basic Commands:

ls whoami echo hello

🔸 Encodings & Piping:

echo "ls /home" | base64 printf "ls /home\n" | bash

🔸 Redirection & Variables:

ls /home > /tmp/output.txt cat /tmp/output.txt export CMD="ls /home" eval $CMD

🔸 Command Substitution:

$(ls) :; ls /home

🔸 Function Definitions (Blocked due to restricted chars like {, /, s):

function foo() { ls /home; } foo

## ✅ Successful Exploit

Despite the blacklist, Bash does not clear the environment or function definitions between inputs. So, a creative use of function injection worked:

### 💡 Step 1: Define a function using allowed characters

UNC_a%%=() {  /usr/bin/env; }

Valid Bash function name

Uses only whitelisted characters

/usr/bin/env was allowed and reveals the environment


### 💡 Step 2: Trigger the function

F

This executed the payload inside the function and printed the environment, which led to recovering the flag.

🎯 Conclusion

Bypassed the blacklist using environment persistence and safe Bash syntax

Lesson: Blacklists are not security. They are duct tape over a broken vault.


## 📚 Key Takeaways

Bash environments persist between inputs unless explicitly reset.

Function names can be bizarre yet valid (UNC_a%%).

Even a seemingly robust character filter is susceptible to logic-layer abuses.

Commands like env can leak massive information even when ls, cat, etc. are restricted.


📌 Pro tip: In CTFs and real systems alike, don't just attack the walls — attack the logic.
