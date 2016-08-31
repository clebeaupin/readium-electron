{
  'includes': [
    'filenames.gypi'
  ],
  'variables': {
    'nacl_sdk_dir': './vendor/nacl_sdk/pepper_49',
    'ppapi_include_dir': '<(nacl_sdk_dir)/include',
    'epub3_root_dir': './vendor/readium-sdk/Platform/cross-platform',
    'epub3_include_dir': '<(epub3_root_dir)/include',
    'libxml2_include_dir': '<(epub3_root_dir)/vendor/libxml2/include'
  },
  'target_defaults': {
    'cflags': [
      '-w',
      '-fPIC',
      '-fvisibility=hidden',
      '-g', # Debug mode
    ],
    'defines': [
      'BUILDING_EPUB3',
      'FEATURES_READIUM'
    ]
  },
  'targets': [
    {
      'target_name': 'readium',
      'type': 'shared_library',
      'include_dirs': [
        '<(ppapi_include_dir)',
        '<(epub3_include_dir)',
        '<(libxml2_include_dir)'
      ],
      'dependencies': [
        'vendor/readium-sdk/Platform/cross-platform/readium.gyp:epub3',
        'ppapi'
      ],
      'sources': [
        'src/readium.cc'
      ]
    },
    {
      'target_name': 'ppapi',
      'type': 'static_library',
      'include_dirs': [
        '<(ppapi_include_dir)'
      ],
      'sources': [
        '<@(ppapi_sources)'
      ]
    }
  ],
  'conditions': [
    ['OS=="mac"', {
        'target_defaults': {
          'defines': [
            'LIBXML_THREAD_ENABLED',
          ],
          'cflags_cc': [
            #'-std=c++0x',
            #'-stdlib=libc++',
            #'-Wtautological-pointer-compare',
            #'-Wc++11-extensions'
          ],
          'xcode_settings': {
            'GCC_TREAT_WARNINGS_AS_ERRORS': 'NO',
            #'MACOSX_DEPLOYMENT_TARGET': '10.8',
            'CLANG_CXX_LANGUAGE_STANDARD': 'gnu++0x',
				    'CLANG_CXX_LIBRARY': 'libc++',
            'WARNING_CFLAGS': [
              '-Wno-unknown-warning-option',
              '-Wno-parentheses-equality',
              '-Wno-unused-function',
              '-Wno-sometimes-uninitialized',
              '-Wno-pointer-sign',
              '-Wno-sign-compare',
              '-Wno-string-plus-int',
              '-Wno-unused-variable',
              '-Wno-deprecated-declarations',
              '-Wno-return-type',
              '-Wno-gnu-folding-constant',
              '-Wno-shift-negative-value',
              '-Wno-tautological-pointer-compare',
              '-Wno-inconsistent-missing-override',
              '-Wno-empty-body',
              '-Wno-uninitialized',
              '-Wno-potentially-evaluated-expression'
            ]
          },
          'ldflags': [

          ],
          'link_settings': {
            'libraries': [
              '-lz',
              #'-licuuc',
              '-liconv',
              '-lpthread',
              '-lcrypto'
            ]
          }
        }
    }],
    ['OS=="linux"', {
        'target_defaults': {
          'defines': [
            'LIBXML_THREAD_ENABLED',
            #'_GLIBCXX_USE_CXX11_ABI=0' # to avoid std::locale issue
          ],
          'cflags': [
            '-m64',
            '-march=x86-64',
          ],
          'cflags_cc': [
            '-std=c++11',
            '-fpermissive'
          ],
          'ldflags': [
            '-m64',
          ],
          'link_settings': {
            'libraries': [
              '-lz',
              '-licuuc',
              '-lpthread',
              '-lcrypto'
            ]
          }
        }
    }],
    ['OS=="win"', {
        'variables': {
          'win_platform_dir': '../Windows/ReadiumSDK/Prebuilt',
          'win_platform_include_dir': '<(win_platform_dir)/Include',
          'win_platform_lib_dir': '<(win_platform_dir)/Lib/x86'
        },
        'target_defaults': {
          'defines': [
            'MSVS_VERSION_2015',
            'NDEBUG',
            'NOMINMAX',
            'WIN32'
          ],
            'msvs_disabled_warnings': [
              4530,
              4577,
              4028,
              4090
            ],
            'msvs_settings': {
              'VCCLCompilerTool': {
                'WarnAsError': 'false',
              },
            },
          'cflags': [
            '/EHsc'
          ],
          'cflags_cc': [
            '-std=c++11',
            '-fpermissive'
          ],
          'include_dirs': [
            '<(win_platform_include_dir)'
          ],
          'link_settings': {
            'library_dirs': [
              '<(win_platform_lib_dir)'
            ],
            'libraries': [
              '-lzlib.lib',
              '-lws2_32.lib',
              '-lmsvcrt.lib',
              '-llegacy_stdio_definitions.lib',
              '-ladvapi32.lib'
            ]
          }
        }
    }],
  ]
}