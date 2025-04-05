
Pod::Spec.new do |s|
  s.name         = 'MyLibrary'
  s.version      = '1.0.0'
  s.summary      = 'A sample iOS library'
  s.description  = 'MyLibrary is a simple iOS framework example.'
  s.homepage     = 'https://github.com/YourUsername/MyLibrary'
  s.license      = { :type => 'MIT', :file => 'LICENSE' }
  s.author       = { 'Your Name' => 'you@example.com' }
  s.source       = { :git => 'https://github.com/YourUsername/MyLibrary.git', :tag => s.version.to_s }

  s.ios.deployment_target = '12.0'
  s.source_files  = 'Classes/**/*.{h,m,swift}'
  s.resources     = 'Resources/*'
end
