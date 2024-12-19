program pascal_hack;

{$APPTYPE CONSOLE}

{$mode Delphi}

// call with fpc -Sd .\pascal_hack.pp ; .\pascal_hack.exe

uses
  SysUtils,
  Generics.Collections;

type
  TStringArray = array of string;
  TCostDict = TDictionary<NativeInt,TDictionary<NativeInt, TDictionary<String, NativeInt>>>;
var
  x: text;
  arr: TStringArray;
  return_array_out: TStringArray;
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
  line:string;

// function WF(height, width:NativeInt): Integer;
//  begin
//   height := 33;
//    WF := 17;
//  end;
function available_directions(pos_x, pos_y: NativeInt; direction: string; directions_x: TDictionary<String, NativeInt>; directions_y: TDictionary<String, NativeInt>; opposite:TDictionary<String, String>; arr: TStringArray): TStringArray;
  type
    TRange = 1..4;
  var
    return_array: TStringArray;
    cardinal: String;
    new_x: NativeInt;
    new_y: NativeInt;    
    neighbour_entry: String;
    dir_string: String;
    rangeValue: integer;
  begin
    dir_string :='NESW';
    SetLength(return_array, 0);
    for rangeValue in TRange do
      begin
      cardinal := dir_string[rangeValue];
      if cardinal <> opposite[direction] then
        begin
          new_x := pos_x + directions_x[direction];
          new_y := pos_y + directions_y[direction];
          neighbour_entry := arr[new_y][new_x];
          if neighbour_entry = '.' then
            begin
            SetLength(return_array, Length(return_array) + 1);
            return_array[High(return_array)] := IntToStr(new_x); 
            SetLength(return_array, Length(return_array) + 1);
            return_array[High(return_array)] := IntToStr(new_y); 
            SetLength(return_array, Length(return_array) + 1);
            return_array[High(return_array)] := cardinal; 
            end;
        end;
      end;
    available_directions := return_array;
  end;

function go_to_next_node(init_x, init_y: NativeInt; cardinal: String; directions_x: TDictionary<String, NativeInt>; directions_y: TDictionary<String, NativeInt>):TStringArray;
var
  score: NativeInt;
  next_node_found: Boolean;
  move_x: NativeInt;
  move_y: NativeInt;
  cur_x: NativeInt;
  cur_y: NativeInt;
  next_x: NativeInt;
  next_y: NativeInt;
  current_cardinal: String;
  av_dir_return: TStringArray;
  return_array: TStringArray;
  return_flag: Boolean;

begin
  score :=0;
  next_node_found:= False;
  move_x := directions_x[cardinal];
  move_y := directions_y[cardinal];
  current_cardinal := cardinal;
  cur_x := init_x + move_x;
  cur_y := init_y + move_y;
  score +=1;
  while not next_node_found do
  begin
    av_dir_return := available_directions(cur_x, cur_y, current_cardinal, directions_x, directions_y, opposite, arr);
    if Length(av_dir_return) = 3 then
    begin
      if av_dir_return[2] = current_cardinal then
        begin
          score += 1;
        end
      else
        begin
        score += 1001;
        end;
      current_cardinal := av_dir_return[2];
      cur_x := StrToInt(av_dir_return[0]);
      cur_y := StrToInt(av_dir_return[1]);
    end
    else if Length(av_dir_return) = 0 then
      begin
        next_x := cur_x + directions_x[current_cardinal];
        next_y := cur_y + directions_y[current_cardinal];
        score += 1;
        return_array := [IntToStr(next_x), IntToStr(next_y), current_cardinal, IntToStr(score)];
        return_flag := True;
      end
    else
      next_node_found := True;

  end;
if not return_flag then
  return_array := [IntToStr(cur_x), IntToStr(cur_y), current_cardinal, IntToStr(score)];
go_to_next_node := return_array;
end;

procedure explore(pos_x, pos_y: NativeInt; cardinal: String; score: NativeInt; directions_x: TDictionary<String, NativeInt>; directions_y: TDictionary<String, NativeInt>; node_costs: TCostDict; opposite:TDictionary<String, String>; arr: TStringArray);
  var
  gtnn_return: TStringArray;
  x_int_key: NativeInt;
  y_int_key: NativeInt;
  contains: Boolean;
  node_x: NativeInt;
  node_y: NativeInt;
  node_card: String;
  node_score: NativeInt;
  av_dir_return: TStringArray;

  begin
    gtnn_return := go_to_next_node(pos_x, pos_y, cardinal, directions_x, directions_y);
    node_x := StrToInt(gtnn_return[0])
    node_y := StrToInt(gtnn_return[1])
    node_card := gtnn_return[2]
    node_score := StrToInt(gtnn_return[3])
    contains:= False;
    for x_int_key in node_costs.keys do
      if x_int_key = node_x then
        for y_int_key in node_costs[x_int_key].keys do
          if y_int_key = node_y then
            contains := True;
    if not contains then
      node_costs[node_x][node_y] := TDictionary<String, NativeInt>.create;
    av_dir_return := available_directions(node_x, node_y, node_card, directions_x, directions_y, opposite, arr);
    // CONTINUE HERE! ITERATE TRHOUGH AV_DIR_RETURN, which is line 126 in pyhack.
    // REMEMBER, available_directions returns a single list, containing sets of three. Separate them out first!
  end


function plug_dead_ends(height, width: NativeInt; directions_x: TDictionary<String, NativeInt>; directions_y: TDictionary<String, NativeInt>; arr: TStringArray): TStringArray;  
  type
    TRange = 1..4;
  var
  rangeValue : integer;
  exit_code: Boolean;
  neighbours: array of string;
  new_x: NativeInt;
  new_y: NativeInt;
  entry: string;
  letter: string;
  num_of_pounds: NativeInt;
  neighbour: string;
  dir_string: string;
  return_array: TStringArray;
  begin
    exit_code := False;
    dir_string :='NESW';
    return_array := ['no change'];
    for row := 0 to height - 1 do
      for column := 0 to width - 1 do
        begin
        entry := arr[row][column];
        if entry = '.' then
          begin
          SetLength(neighbours, 0);
          for rangeValue in TRange do
            begin
              letter := dir_string[rangeValue];
              new_x := column + directions_x[letter];
              new_y := row + directions_y[letter];
              SetLength(neighbours, Length(neighbours) + 1);
              neighbours[High(neighbours)] := arr[new_y][new_x];
            end;
          num_of_pounds := 0;
          for neighbour in neighbours do
            if neighbour = '#' then
              num_of_pounds := num_of_pounds + 1;
          if num_of_pounds = 3 then
            begin
              exit_code := True;
              arr[row][column] := '#';
              return_array := arr
            end;
          end;
        end;
    plug_dead_ends := return_array;
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

  node_costs := TCostDict.create;
  // (x,y) : S: cost
  // x: y: S: cost

  // writeln(height);
  // WF(height, width);
  // writeln(height);
  // for line in arr do
  //   writeln(line);

  return_array_out := arr ;
  while High(return_array_out) > 2 do
    begin
    // writeln(High(return_array_out));
    arr:= return_array_out;
    return_array_out := plug_dead_ends(height, width, directions_x, directions_y, arr);
    end;
  // writeln(exit_code);
  // for line in arr do
  //   writeln(line);


end.