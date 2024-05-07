#!/usr/bin/env ruby
#puts ARGV[0].scan(/[^"]\b\d{10,10}\b/).join
puts ARGV[0].scan(/^\d{10}$/).join
