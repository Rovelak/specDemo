# Hook Claude Code — log prompts to a file
# PowerShell version for Windows

$LogFile = Join-Path $env:USERPROFILE ".claude\prompt_history.log"

# Ensure the directory exists
$LogDir = Split-Path $LogFile -Parent
if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
}

# Read the JSON hook input from stdin
$HookInput = [Console]::In.ReadToEnd()

try {
    # Parse JSON and extract the prompt
    $Json = $HookInput | ConvertFrom-Json
    $Prompt = $Json.prompt

    # Create timestamp in ISO 8601 format (UTC)
    $Timestamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

    # Create log entry
    $LogEntry = @{
        timestamp = $Timestamp
        prompt = $Prompt
    } | ConvertTo-Json -Compress

    # Append to log file
    Add-Content -Path $LogFile -Value $LogEntry -Encoding UTF8

} catch {
    # If parsing fails, log the error but don't block the hook
    $ErrorMsg = "Error logging prompt: $_"
    Write-Error $ErrorMsg
}

# Exit successfully
exit 0
