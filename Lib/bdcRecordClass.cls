VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "bdcRecordClass"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = True
#Const USE_TEST_DATA = True
Option Explicit
''/****************************************************************************
'' Class: bdcRecordClass
''=============================================================================
'-
'-   Copyright (c) 1999 - 2005 by Barry Dancis Consulting, Inc.
'-   Licensed to Monell according to the
'-   LIMITED SOFTWARE ASSIGNMENT AND LICENSE AGREEMENT of January 5, 2005
'-
'' Purpose : A dictionary with static keys that can be accessed by key (string)
''          or Enum (index).
'' Limits: Lacks an iterator - this will be a problem if processed in
''           a shop. Think about putting one back in
''         ASSUMES ENUM BEGINS AT 1 AND FOLLOWS IN SEQUENCE - SHOULD BE MODIFIED
''         SO THAT ENUM CAN BEGIN ANYWHERE AND THEN INCREASE BY ONES.
'-
'-                            Modification History
'-  11Nov2004  Adapted from StaticDictionaryClass. Barry Martin Dancis
'-  20Dec2004  Basic unit is Field, but added dictionary Item accessors. BMD
'-  21Mar2015  Fixed ItemExists to use myFieldNames to look for item. BMD
'-  19Feb2016  Renamed Clone to CloneShallow and fixed code. BMD
'-  04Apr2016  Created Property Let Items to allow filling myFields all at once. BMD
''=============================================================================
'' Description: The Record class acts as a dictionary but actually stores its
''   values in a base 1 variant array indexed by the field key. The keys must be
''   integers (or longs) and can be used for sequential traversal so there must
''   be no gaps in their sequence. The value of NO_ENUM must be zero. Access of
''   fields can be through the keys or the field names. Field names and keys can
''   be interconverted
''      Dictionary     bdcRecordClass
''         keys          fieldnames - ascii key
''         items         fields     - value
''                       fieldkeys  - integer
Const DEFAULT_CLASS_NAME = "bdcRecordClass"
Option Base 1 'All arrays have a base of 1
Const BAD_FIELD_KEY = 32701
Const BAD_FIELD_NAME = 32702
Const FIRST_ENUM = 1

Private myFields() As Variant 'Array - Index: Enum,   Value: Field value
Private myFieldName As Dictionary ' Key:   Enum,      Value: FieldName
Private myFieldKey As Dictionary  ' Key:   FieldName, Value: Enum
Private myName As String
'------------------------------------------------------------------------------
Public Sub Initialize(ByVal newClassName As String, ByVal FirstKey As Long, ByVal FieldNames As Variant)
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "Initialize"
'------------------------------------------------------------------------------
Dim i, First_ As Long

  CLASS_NAME = newClassName
  First_ = LBound(FieldNames)
  For i = First_ To UBound(FieldNames)
    Add FieldNames(i), FirstKey + i - First_
  Next i
'------------------------------------------------------------------------------
End Sub
'------------------------------------------------------------------------------
Public Sub Add(ByVal newFieldName As String, ByVal FieldKey As Long, Optional ByVal newValue As Variant)
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "Add"
  Const DUPLICATE_KEY = 32601
  Const DUPLICATE_NAME = 32602
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------

  If myFieldKey.Count > 0 And _
     FieldKey <> (myFieldKey.Count + 1) Then
    Err.Raise BAD_FIELD_KEY, , "Enum out of order <Key: " & CStr(FieldKey) & ", Name: " & newFieldName & ">"
  End If
  If myFieldKey.Exists(newFieldName) Then
    Err.Raise DUPLICATE_KEY, , _
     "Enumerated key already present in " & CLASS_NAME & "<Key: " & CStr(FieldKey) & ", Name: " & newFieldName & ">"
  End If
  
  If myFieldName.Exists(FieldKey) Then
    Err.Raise DUPLICATE_NAME, , _
    "Field name already present in " & CLASS_NAME & "<Key: " & CStr(FieldKey) & ", Name: " & newFieldName & ">"
  End If
  
  ReDim Preserve myFields(FieldKey)
  
  If IsObject(newValue) Then
    Set myFields(FieldKey) = newValue
  Else
    myFields(FieldKey) = newValue
  End If
  myFieldName.Item(FieldKey) = newFieldName
  myFieldKey.Item(newFieldName) = FieldKey
  
Exit Sub
'------------------------------------------------------------------------------
ErrorHandler:
  SystemError.Raise Err.Number, PROCEDURE_NAME, Err.Description
Exit Sub
'------------------------------------------------------------------------------
End Sub
''=============================================================================
''Public Function BadKeyMessage
''Purpose : Creates text for reporting a bad key
''[in    ]: FieldKey - bad FieldKey
''[in    ]: MessageBody - text to be added to bad key message
''[return]: Text reporting a bad key
''Limits  : None
'------------------------------------------------------------------------------
Public Function BadKeyMessage(ByVal FieldKey As Long, Optional ByVal MessageBody As String) As String
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "BadKeyMessage"
'------------------------------------------------------------------------------
Dim FieldNameText As String
  
  FieldNameText = vbNullString
  If myFieldName.Exists(FieldKey) Then _
    FieldNameText = ", FieldName: " & myFieldName.Item(FieldKey)
  
  BadKeyMessage = "Bad key: " & MessageBody & "<Key: " & FieldKey & FieldNameText & ">"
  
'------------------------------------------------------------------------------
End Function
''=============================================================================
Public Function BoundList(ByVal LeftBound As String, ByVal Separator As String, ByVal RightBound As String) As String
'------------------------------------------------------------------------------
  BoundList = LeftBound & List(Separator) & RightBound
'------------------------------------------------------------------------------
End Function
''=============================================================================
Private Sub Clear(Optional ByVal FieldKey As Long)
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "Clear"
'------------------------------------------------------------------------------
  If IsMissing(FieldKey) Then 'Clear all physical fields
    ClearAll
  Else
    ClearField FieldKey
  End If
'------------------------------------------------------------------------------
End Sub
''=============================================================================
Private Sub ClearField(ByVal FieldKey As Long)
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "ClearField"
  Const BAD_FIELD_NAME = 32601
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------

  If Not Exists(FieldKey) Then Err.Raise BAD_FIELD_KEY, , PROCEDURE_NAME
    
    If IsObject(myFields(FieldKey)) Then
      Set myFields(FieldKey) = Nothing
    Else
      myFields(FieldKey) = Null
    End If
Exit Sub
'------------------------------------------------------------------------------
ErrorHandler:
  
  Err.Raise Err.Number, Class_ProcedurePath(PROCEDURE_NAME), Err.Description
  
Exit Sub
'------------------------------------------------------------------------------
End Sub
''=============================================================================
Private Sub ClearAll()
'------------------------------------------------------------------------------
Dim i As Long
  For i = LBound(myFields) To UBound(myFields)
    ClearField (i)
  Next i
'------------------------------------------------------------------------------
End Sub
''=============================================================================
''Public Function CloneShallow
''Purpose : Return CloneShallow of current instance
''[in    ]: ClassName
''[   out]: None
''[return]: CloneShallow of instance if successful, Nothing otherwise
''Limits  : Object items in new record point to same object items in old record
'------------------------------------------------------------------------------
Public Function CloneShallow(Optional ByVal ClassName As String = NO_STRING) As bdcRecordClass
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "CloneShallow"
  Const BAD_KEY = 32601
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------
Dim newRecord As New bdcRecordClass
Dim FieldKey As Variant

  If ClassName = NO_STRING Then
    ClassName = CLASS_NAME
  End If
  newRecord.Initialize ClassName, FIRST_ENUM, FieldNames
  For Each FieldKey In myFieldName.Keys
    If IsObject(myFields(FieldKey)) Then
      Set newRecord.Field(FieldKey) = myFields(FieldKey)
'      If myFields(FieldKey) Is Nothing Then
'        Set newRecord.Field(FieldKey) = Nothing
'      Else
'        Set newRecord.Field(FieldKey) = myFields(FieldKey).CloneShallow
'      End If
    Else
      newRecord.Field(FieldKey) = myFields(FieldKey)
    End If
  Next FieldKey

  Set CloneShallow = newRecord
  
Exit Function
'------------------------------------------------------------------------------
ErrorHandler:
  
  Err.Raise Err.Number, Class_ProcedurePath(PROCEDURE_NAME), Err.Description
  Set CloneShallow = Nothing
  
Exit Function
'------------------------------------------------------------------------------
End Function 'CloneShallow
''=============================================================================
Public Property Get Count() As Long
'------------------------------------------------------------------------------
  Count = myFieldKey.Count 'This should be the same as ubound(myFields)
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Function Exists(ByVal FieldId As Variant, Optional ByRef aFieldKey As Long, Optional ByRef aFieldName As String) As Boolean
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "Exists"
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------
  If VarType(FieldId) = vbString Then
    aFieldKey = FieldKey(FieldId)
  Else
    aFieldKey = FieldId
  End If

  aFieldName = FieldName(aFieldKey)
  Exists = myFieldName.Exists(aFieldKey)
Exit Function
'------------------------------------------------------------------------------
ErrorHandler:
  Exists = False
Exit Function
'------------------------------------------------------------------------------
End Function
''=============================================================================
'Assumes: Valid input newFieldKey
Public Property Get Field(ByVal FieldId As Variant) As Variant
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "Field (Get)"
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------
Dim NextField As Variant

  If Not getField(FieldId, NextField) Then _
    Err.Raise BAD_FIELD_KEY, , Me.BadKeyMessage(FieldId, "Cannot retrieve Field")
  
  If IsObject(NextField) Then
    Set Field = NextField
  Else
    Field = NextField
  End If

Exit Property
'------------------------------------------------------------------------------
ErrorHandler:
  Err.Raise Err.Number, Class_ProcedurePath(PROCEDURE_NAME), Err.Description
Exit Property
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Property Let Field(ByVal FieldId As Variant, newValue As Variant)
'Assumes: Valid input FieldKey
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "Field (Let)"
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------
Dim myFieldKey As Long
Dim myFieldName As String
  
  If Not Exists(FieldId, myFieldKey, myFieldName) Then _
    Err.Raise BAD_FIELD_KEY, , PROCEDURE_NAME
  
  myFields(myFieldKey) = newValue

Exit Property
'------------------------------------------------------------------------------
ErrorHandler:
  Err.Raise Err.Number, Class_ProcedurePath(PROCEDURE_NAME), Err.Description
Exit Property
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Property Set Field(ByVal FieldId As Variant, newValue As Variant)
'Assumes: Valid input FieldKey
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "Field (Set)"
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------
Dim myFieldKey As Long
Dim myFieldName As String
  
  If Not Exists(FieldId, myFieldKey, myFieldName) Then _
    Err.Raise BAD_FIELD_KEY, , PROCEDURE_NAME

  Set myFields(myFieldKey) = newValue

Exit Property
'------------------------------------------------------------------------------
ErrorHandler:
  Err.Raise Err.Number, Class_ProcedurePath(PROCEDURE_NAME), Err.Description
Exit Property
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Function FieldKey(ByVal FieldName As String) As Long
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "FieldKey"
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------

  If Not myFieldKey.Exists(FieldName) Then Err.Raise BAD_FIELD_NAME
  
  FieldKey = myFieldKey.Item(FieldName)

Exit Function
'------------------------------------------------------------------------------
ErrorHandler:
  FieldKey = 0
  
  Err.Raise BAD_FIELD_NAME, Class_ProcedurePath(PROCEDURE_NAME), "Field does not exist <" & FieldName & ">"
Exit Function
'------------------------------------------------------------------------------
End Function
''=============================================================================
Public Function FieldName(ByVal FieldKey As Variant) As String
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "FieldName"
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------

  If Not myFieldName.Exists(FieldKey) Then _
    Err.Raise BAD_FIELD_KEY
    
  FieldName = myFieldName.Item(FieldKey)
  
Exit Function
'------------------------------------------------------------------------------
ErrorHandler:
  FieldName = vbNullString
  
  Err.Raise BAD_FIELD_KEY, Class_ProcedurePath(PROCEDURE_NAME), Me.BadKeyMessage(FieldKey, "No field for key")
Exit Function
'------------------------------------------------------------------------------
End Function
''=============================================================================
Public Function FieldNameList(ByVal Separator As String) As String
'------------------------------------------------------------------------------
  FieldNameList = Join(FieldNames, Separator)
'------------------------------------------------------------------------------
End Function
''=============================================================================
Public Function FieldKeys() As Variant
'------------------------------------------------------------------------------
  FieldKeys = myFieldKey.Items
'------------------------------------------------------------------------------
End Function
''=============================================================================
Public Function FieldNames() As Variant
'------------------------------------------------------------------------------
  FieldNames = myFieldName.Items
'------------------------------------------------------------------------------
End Function
''=============================================================================
Public Property Get Fields() As Variant
'------------------------------------------------------------------------------
  Fields = myFields
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Property Let Fields(newFields As Variant)
'------------------------------------------------------------------------------
  Items = newFields
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Function getField(ByVal FieldId As Variant, ByRef aField As Variant) As Boolean
'Purpose : Get value for input FieldId
'Return : True is valid id, False otherwise
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "getField"
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------
Dim myFieldKey As Long
Dim myFieldName As String
  
  If Not Exists(FieldId, myFieldKey, myFieldName) Then _
    Err.Raise BAD_FIELD_KEY, , PROCEDURE_NAME
  
  If IsObject(myFields(myFieldKey)) Then
    Set aField = myFields(myFieldKey)
  Else
    aField = myFields(myFieldKey)
  End If

  getField = True

Exit Function
'------------------------------------------------------------------------------
ErrorHandler:
  
  getField = False
  If IsObject(aField) Then
    Set aField = Nothing
  Else
    aField = Null
  End If
  
Exit Function
'------------------------------------------------------------------------------
End Function
''=============================================================================
Public Function ItemExists(ByVal NextItem As Variant) As Boolean
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "ItemExists"
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------
  ItemExists = ItemKey(NextItem) > 0
Exit Function
'------------------------------------------------------------------------------
ErrorHandler:
  
  ItemExists = False
  
Exit Function
'------------------------------------------------------------------------------
End Function
''=============================================================================
Public Function ItemKey(ByVal NextItem As Variant) As Long
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "ItemKey"
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------
Dim i As Integer

  For i = LBound(myFields) To UBound(myFields)
    If myFieldName(i) = NextItem Then
      ItemKey = i
      Exit Function
    End If
  Next i
  Err.Raise BAD_FIELD_NAME
Exit Function
'------------------------------------------------------------------------------
ErrorHandler:
  ItemKey = 0
  
  Err.Raise BAD_FIELD_NAME, Class_ProcedurePath(PROCEDURE_NAME), "Field does not exist <" & NextItem & ">"
Exit Function
'------------------------------------------------------------------------------
End Function
''=============================================================================
''        Procedures To Make Class Compatible with Dictionary Calls
''=============================================================================
'''Public Function NewEnum() As IUnknown
'''  Set NewEnum = myFieldKey.[_NewEnum]
'''End Function
''=============================================================================
Public Property Get Item(ByVal ItemKey As Variant) As Variant
'Assumes: Valid existing input ItemKey
'------------------------------------------------------------------------------
  If IsObject(Field(ItemKey)) Then
    Set Item = Field(ItemKey)
  Else
    Item = Field(ItemKey)
  End If
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Property Let Item(ByVal ItemKey As Variant, newValue As Variant)
'Assumes: Valid existing input ItemKey
'------------------------------------------------------------------------------
  Field(ItemKey) = newValue
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Property Set Item(ByVal ItemKey As Variant, newValue As Variant)
'Assumes: Valid existing input ItemKey
'------------------------------------------------------------------------------
  Set Field(ItemKey) = newValue
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Property Get Items() As Variant
'------------------------------------------------------------------------------
  Items = myFields
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Property Let Items(newItems As Variant)
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "Items"
  Const WRONG_ITEM_COUNT = 32601
  On Error GoTo ErrorHandler
'------------------------------------------------------------------------------
Dim i, First_ As Long
Dim NextItem As Variant

  If Array_Size(newItems) <> myFieldKey.Count Then  '
    Err.Raise WRONG_ITEM_COUNT, , "Number of newItems must be " & Bracket(myFieldKey.Count) & _
                               " and not " & Bracket(Array_Size(newItems))
  End If
  
  i = LBound(myFields)
  For Each NextItem In newItems
    myFields(i) = NextItem
    i = i + 1
  Next
'  Debug.Print List("##")
Exit Property
'------------------------------------------------------------------------------
ErrorHandler:
  SystemError.Raise Err.Number, PROCEDURE_NAME, Err.Description
Exit Property
'------------------------------------------------------------------------------
End Property
''=============================================================================
Public Function Keys() As Variant
'------------------------------------------------------------------------------
  Keys = myFieldName.Items
'------------------------------------------------------------------------------
End Function
''=============================================================================
Public Function List(ByVal Separator As String) As String
'------------------------------------------------------------------------------
  Const PROCEDURE_NAME = "List"
'------------------------------------------------------------------------------
  List = Join(myFields, Separator)
'------------------------------------------------------------------------------
End Function
''=============================================================================
Public Sub UpdateFields(ByVal FieldIterator As Object)
'Purpose : To update fields in the item with all fields in the FieldIterator
'            This is necessary for the Shop
'------------------------------------------------------------------------------
Dim FieldKey As Variant
Dim FieldValue As Variant

Err.Raise 32222, "UpdateFields", "Error - Sub not working!!"

  FieldKey = Null
  Do While FieldIterator.GetNext(FieldKey, FieldValue)
    If IsObject(FieldValue) Then
      Set myFields(FieldKey) = FieldValue
    Else
      myFields(FieldKey) = FieldValue
    End If
  Loop
  
End Sub
''=============================================================================
''                               Class Procedures
''=============================================================================
Private Sub Class_Finish()
  Set myFieldKey = Nothing
  Set myFieldName = Nothing
End Sub
''=============================================================================
Public Property Get CLASS_NAME() As String
  If myName = NO_STRING Then
    CLASS_NAME = DEFAULT_CLASS_NAME
  Else
    CLASS_NAME = myName
  End If
End Property
''=============================================================================
Public Property Let CLASS_NAME(newValue As String)
  myName = newValue
End Property
''=============================================================================
Private Function Class_ProcedurePath(ByVal ProcedureName As String) As String
  Class_ProcedurePath = CLASS_NAME & ">" & ProcedureName
End Function
''=============================================================================
Private Sub Class_Start()
  Erase myFields
  Set myFieldKey = New Dictionary
  Set myFieldName = New Dictionary
End Sub
''=============================================================================
Private Sub Class_Initialize()
  Class_Start
End Sub


