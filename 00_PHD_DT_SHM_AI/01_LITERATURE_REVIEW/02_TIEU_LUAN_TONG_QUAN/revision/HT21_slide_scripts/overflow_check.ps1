param([string]$src, [string]$outCsv)
# Đo chữ tràn: so chiều cao chữ (BoundHeight) với chiều cao ô trừ lề; với ô không ngắt dòng, so chiều rộng.
$app = New-Object -ComObject PowerPoint.Application
$pre = $app.Presentations.Count
$pr = $app.Presentations.Open($src, $true, $false, $false)
$rows = @()
function Check($sh, $i) {
    if ($sh.Type -eq 6) { foreach ($c in $sh.GroupItems) { Check $c $i }; return }
    if (-not $sh.HasTextFrame) { return }
    $tf = $sh.TextFrame2
    if (-not $tf.HasText) { return }
    $tr = $tf.TextRange
    $availH = $sh.Height - $tf.MarginTop - $tf.MarginBottom
    $availW = $sh.Width - $tf.MarginLeft - $tf.MarginRight
    $overH = $tr.BoundHeight - $availH
    $overW = 0
    if ($tf.WordWrap -eq 0) { $overW = $tr.BoundWidth - $availW }
    $minSize = 999
    foreach ($r in $tr.Runs()) { if ($r.Text.Trim().Length -gt 0 -and $r.Font.Size -lt $minSize) { $minSize = $r.Font.Size } }
    if ($overH -gt 1 -or $overW -gt 1) {
        $t = $tr.Text -replace "`r", ' / '
        if ($t.Length -gt 70) { $t = $t.Substring(0, 70) }
        $script:rows += [pscustomobject]@{slide=$i; id=$sh.Id; overH=[math]::Round($overH,1); overW=[math]::Round($overW,1); h=[math]::Round($sh.Height/72,2); w=[math]::Round($sh.Width/72,2); top=[math]::Round($sh.Top/72,2); minpt=$minSize; text=$t}
    }
}
for ($i = 1; $i -le $pr.Slides.Count; $i++) { foreach ($sh in $pr.Slides.Item($i).Shapes) { Check $sh $i } }
$pr.Close(); if ($pre -eq 0) { $app.Quit() }
$rows | Export-Csv -Path $outCsv -NoTypeInformation -Encoding UTF8
"overflows=" + $rows.Count
