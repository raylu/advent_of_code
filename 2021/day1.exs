inp = File.stream!("day1_input") |> Stream.map(&String.trim_trailing(&1)) |> Stream.map(&String.to_integer(&1))
increases = Enum.reduce inp, {0, nil}, fn
	line, {0, nil} -> {0, line}
	line, {increases, prev} when line > prev -> {increases + 1, line}
	line, {increases, prev} when line <= prev -> {increases, line}
end
IO.inspect(elem(increases, 0))
