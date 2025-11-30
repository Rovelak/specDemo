# Hook Claude Code — log des prompts dans un fichier

LOGFILE="$HOME/.claude/prompt_history.log"

# Lire le JSON du hook depuis stdin
read -r HOOK_INPUT

# Extraire le prompt (avec jq, ou à minima grep)
PROMPT=$(echo "$HOOK_INPUT" | grep -Po '"prompt":\s*"\K[^"]*')

# Horodatage
TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Append au log
echo "{\"timestamp\": \"$TS\", \"prompt\": \"$(echo "$PROMPT" | sed 's/"/\\"/g')\"}" >> "$LOGFILE"

# Sortie normale
exit 0