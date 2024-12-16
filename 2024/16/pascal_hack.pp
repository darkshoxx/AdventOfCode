program pascal_hack;

{$APPTYPE CONSOLE}

{$mode Delphi}

// call with fpc -Sd .\pascal_hack.pp ; .\pascal_hack.exe

uses
  SysUtils,
  Generics.Collections;

var
  x: text;
  arr: array of string;
  height: NativeInt;
  width: NativeInt;
  row: NativeInt;
  column: NativeInt;
  start_x: NativeInt;
  start_y: NativeInt;
  end_x: NativeInt;
  end_y: NativeInt;
  opposite: TDictionary<String, String>;
  directions_x: TDictionary<String, NativeInt>;
  directions_y: TDictionary<String, NativeInt>;
  exit_code: Boolean;

function WF(height, width:NativeInt): Integer;
 begin
   WF := 17;
 end;

function plug_dead_ends(height, width: NativeInt; directions: TDictionary; arr: array1`q2 wa): Boolean;  begin
  writeln('2222');
  plug_dead_ends := True;
  end;

begin

  // Load file to string array (old and inefficient way)
  AssignFile(x, 'input_small.txt');
  Reset(x);
  try
    while not Eof(x) do
    begin
      SetLength(arr, Length(arr) + 1);
      Readln(x, arr[High(arr)]);
    end;
  finally
    CloseFile(x);
  end;
  // this is where it starts
  height := Length(arr);
  width := Length(arr[0]);
  for row := 0 to height - 1 do
    for column := 0 to width - 1 do
      begin
        if arr[row][column] = 'S' then
          begin
            start_x := row;
            start_y := column;
          end;
        if arr[row][column] = 'E' then
          begin
            end_x := row;
            end_y := column;
          end;
      end;
  writeln(end_x);
  writeln(end_y);
  opposite := TDictionary<String, String>.create;
  opposite.add('N', 'S');
  opposite.add('S', 'N');
  opposite.add('W', 'E');
  opposite.add('E', 'W');
  directions_x := TDictionary<String, NativeInt>.create;
  directions_x.add('N', 0);
  directions_x.add('S', 0);
  directions_x.add('W', -1);
  directions_x.add('E', 1);
  directions_y := TDictionary<String, NativeInt>.create;
  directions_y.add('N', -1);
  directions_y.add('S', 1);
  directions_y.add('W', 0);
  directions_y.add('E', 0);
  writeln(directions_y['N']);


  // WF(height, width);
  exit_code := plug_dead_ends(height, width, directions, arr);
  writeln(exit_code);

end.