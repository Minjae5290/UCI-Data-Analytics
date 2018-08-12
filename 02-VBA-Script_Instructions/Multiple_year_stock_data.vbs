Sub Multiple_year_stock_data():

For Each ws In Worksheets

    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Total Stock Volume"


        Dim Lastrow As Long
        Lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        
            Randomize
            Dim R As Long
            For R = 2 To Lastrow
            ws.Cells(R, 11).Value = Chr(Int(Rnd * 26) + 65)
            Next R
                               
        
        For i = 2 To Lastrow
            ws.Cells(i, 9).Value = ws.Cells(i, 1).Value + ws.Cells(i, 11).Value
            ws.Cells(i, 10).Value = ws.Cells(i, 6).Value * ws.Cells(i, 7).Value
        Next i

    ws.Range("J1").CurrentRegion.EntireColumn.AutoFit
    ws.Columns(11).Hidden = True
    
Next ws

End Sub