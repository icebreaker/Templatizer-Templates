require 'test/unit'
require '%FILENAME%'

class %CLASSNAME%Test < Test::Unit::TestCase
  def test_version
    assert_equal %CLASSNAME%::VERSION, '0.1.0'
  end
end
