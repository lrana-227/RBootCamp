


Sub Alpha_Results()
  For Each ws In Worksheets
    
    ' Set an initial variable for holding the ticker name
      Dim Ticker_Name As String
    
    ' Set an initial variable for holding the yearly change
      Dim yearly_change As Double
      yearly_change = 0
      
    ' Set an initial variable for holding the percent change
      Dim percent_change As Double
      percent_change = 0
      
    ' Set an initial variable for holding the total stock volume
      Dim stock_volume As Double
      stock_volume = 0

    ' Keep track of the location for each ticker in the summary table
      Dim Summary_Table_Row As Integer
      Summary_Table_Row = 2
      
      'Keep track of hoq many rows
      Dim rowcount As Integer
      rowcount = 0

    ' Set numrows = number of rows of data.
      NumRows = ws.Range("A2", ws.Range("A2").End(xlDown)).Rows.Count
      
    'Heading Names
      ws.Range("I1") = "Ticker"
      ws.Range("J1") = "Yearly Change"
      ws.Range("K1") = "Percent Change"
      ws.Range("L1") = "Total Stock Volume"
      
    
    ' Loop through all sheets
        
    
    For i = 2 To NumRows
        
        ' Check if we are still within the same ticker, if it is not...
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
        
              ' Set the ticker name
              Ticker_Name = ws.Cells(i, 1).Value
        
              ' Add to the Stock Volume
              stock_volume = stock_volume + ws.Cells(i, 7).Value
              
              ' Add to the Yearly Change
              yearly_change = (ws.Cells(i, 6) - ws.Cells(i - rowcount, 3))
              
              ' Add to the Percent Change
              If ws.Cells(i, 6) <> 0 And ws.Cells(i - rowcount, 3) <> 0 Then
                percent_change = yearly_change / ws.Cells(i - rowcount, 3)
                End If
              ' Print the Ticker in the Summary Table
              ws.Range("I" & Summary_Table_Row).Value = Ticker_Name
              
              ' Print the Ticker in the Summary Table
              ws.Range("J" & Summary_Table_Row).Value = yearly_change
        
              ' Print the Ticker in the Summary Table
              ws.Range("K" & Summary_Table_Row).Value = percent_change
              ws.Range("K" & Summary_Table_Row).NumberFormat = "0.00%"
              
              ' Print the Brand Amount to the Summary Table
              ws.Range("L" & Summary_Table_Row).Value = stock_volume
        
              ' Add one to the summary table row
              Summary_Table_Row = Summary_Table_Row + 1
              
              ' Reset the Brand Total
              stock_volume = 0
             ' yearly_change = 0
              'percent_change = 0
              rowcount = 0
              
            ' If the cell immediately following a row is the same brand...
            Else
        
              ' Add to the Brand Total
              stock_volume = stock_volume + ws.Cells(i, 7).Value
              rowcount = rowcount + 1
              'yearly_change = (ws.Cells(i, 3) - ws.Cells(i, 6)) + yearly_change
              
              'If yearly_change <> 0 Then
                'percent_change = yearly_change / ws.Cells(i, 3)
                
                'End If
        
        End If
        
     

    Next i
    
     ws.Columns("I:L").AutoFit
  Next ws

    Call format
End Sub

Sub format()
For Each ws In Worksheets

Dim rg As Range
Dim cond1 As FormatCondition
Dim cond2 As FormatCondition

Set rg = ws.Range("J2", ws.Range("J2").End(xlDown))



'define the rule for each conditional format
Set cond1 = rg.FormatConditions.Add(xlCellValue, xlGreater, "0")
Set cond2 = rg.FormatConditions.Add(xlCellValue, xlLess, "0")


'define the format applied for each conditional format
With cond1
.Interior.Color = vbGreen
End With

With cond2
.Interior.Color = vbRed
End With

Next ws
 Call Bonus
End Sub

Sub Bonus()
For Each ws In Worksheets
    Dim greatest_percent As Double
    greatest_percent = 0
    
    Dim lowest_percent As Long
    lowest_percent = ws.Range("K11").Value
    
    Dim greatest_volume As Long
    greatest_volume = 0
    
    Dim sum_table_lastrow_year_change As Integer
    sum_table_lastrow = ws.Range("J2", ws.Range("J2").End(xlDown))
    
    
    For j = 2 To sum_table_lastrow_year_change
        
        If ws.Cells(j, 11).Value > greatest_percent Then
            ws.Cells(j, 11).Value = greatest_percent
            ws.Range("O2") = greatest_percentage
            ws.Range("P2") = ws.Cells(j, 9).Value
        End If
        If ws.Cells(j, 11).Value < lowest_percent Then
            ws.Cells(j, 11).Value = lowest_percent
            ws.Range("O3") = lowest_percent
            ws.Range("P3") = ws.Cells(j, 9).Value
        End If
        If ws.Cells(j, 12).Value > greatest_volume Then
            ws.Cells(j, 12).Value = greatest_volume
            ws.Range("O4") = greatest_volume
            ws.Range("P4") = ws.Cells(j, 9).Value
        End If
    Next j
    
    ws.Range("N2") = "Yearly Change"
    ws.Range("N3") = "Percent Change"
    ws.Range("N4") = "Total Stock Volume"
    
    
Next ws
End Sub

