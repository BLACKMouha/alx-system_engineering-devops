#!/usr/bin/env ruby
#puts ARGV[0].scan(/(from:[[\w]+|[\+[\d]]]+)/).join(',')
puts ARGV[0].scan(/\[from:([[\w]+|[\+[\d]]]+)\].+\[to:([\+\d]+)\].+\[flags:([-?\d\:]+)\]/).join(',')
