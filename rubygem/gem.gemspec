Kernel.load './lib/%FILENAME%/version.rb'

Gem::Specification.new '%FILENAME%', %CLASSNAME%::VERSION do |s|
  s.rubyforge_project = '%FILENAME%'
  s.authors           = ['%AUTHOR%']
  s.email             = ['%EMAIL%']
  s.description       = '%DESCRIPTION%'
  s.homepage          = 'http://github.com/%GITHUB%/%NAME%'
  s.rdoc_options      = ["--charset=UTF-8"]
  s.extra_rdoc_files  = %w[README.md LICENSE]
  s.require_paths     = ['lib']
  s.files             = Dir.glob('lib/**/*') + %w(README.md LICENSE)
  s.test_files        = Dir.glob('test/**/*')
  s.executables       = ['%FILENAME%']
  #s.add_runtime_dependency('yourgem', ">= 1.0.0")
  #s.add_development_dependency('yourgem', ">= 1.0.0")
  s.summary           = '%DESCRIPTION%'
end
