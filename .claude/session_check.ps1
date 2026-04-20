$logFile = "C:\Users\gussa\Desktop\oneteam\amateras\아마테라스\메모\session_log.md"
$today = (Get-Date -Format "yyyy-MM-dd")
if (Select-String -Path $logFile -Pattern $today -Quiet) {
    exit 0
} else {
    Write-Output "No session log for $today. Please write summary now."
    exit 2
}