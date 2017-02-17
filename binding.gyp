{
    "targets": [
        {
            "target_name": "R",
            "sources": ["src/rl.cpp",
                        "src/rlink.cpp"],
            "variables": {
                'R_HOME%': '<!(R RHOME)',
                'RCPPFLAGS%': '<!(<(R_HOME%)/bin/R CMD config --cppflags | sed "s/-I\///")',
                'RLDFLAGS%': '<!(<(R_HOME%)/bin/R CMD config --ldflags | sed "s/-I\///")',
                'RBLAS%': '<!(<(R_HOME%)/bin/R CMD config BLAS_LIBS | sed "s/-I\///")',
                'RLAPACK%': '<!(<(R_HOME%)/bin/R CMD config LAPACK_LIBS | sed "s/-I\///")',
                'RINSIDEINCL%': '<!(<(R_HOME%)/bin/R --vanilla --slave -e "RInside:::CxxFlags()" | sed "s/-I\///")',
                'RINSIDELIBS%': '<!(<(R_HOME%)/bin/R --vanilla --slave -e "RInside:::LdFlags()")',
                'RCPPINCL%': '<!(<(R_HOME%)/bin/R --vanilla --slave -e "Rcpp:::CxxFlags()" | sed "s/-I\///")',
                'RCPPLIBS%': '<!(<(R_HOME%)/bin/R --vanilla --slave -e "Rcpp:::LdFlags()")',
            },
            "link_settings":
            {
                'ldflags': [
                    '<(RLDFLAGS)'
                ],
                'libraries': [
                    '<(RLDFLAGS)',
                    '<(RINSIDELIBS)',
                    '<(RCPPLIBS)',
                    '<(RBLAS)',
                    '<(RLAPACK)',
                ],
            },
            "defines": [
                'RINSIDE_CALLBACKS',
            ],
            'include_dirs': [
                "<!(node -e \"require('nan')\")",
                '/<(RINSIDEINCL)',
                '/<(RCPPINCL)',
                '/<(RCPPFLAGS)',
            ],

            'cflags_cc!': ['-fno-rtti', '-fno-exceptions'],
            'cflags_cc+': ['-frtti', '-fno-exceptions'],
            'cflags': ['-std=c++1', '-stdlib=libc++'],
            'conditions': [
                ['OS!="win"', {
                    "defines": [
                        # 'RINSIDE_CALLBACKS',
                    ],
                    'cflags+': ["-std=c++11"],
                    'cflags_c': ["-std=c++11"],
                    'cflags_cc': ["-std=c++11"],
                }],
                ['OS=="mac"', {
                    'xcode_settings': {
                        "MACOSX_DEPLOYMENT_TARGET": "10.12",
                        "defines": [
                            # 'RINSIDE_CALLBACKS'
                        ],
                        "OTHER_CPLUSPLUSFLAGS": [
                            "-stdlib=libc++",
                            "-std=c++11"
                        ],
                        "OTHER_LDFLAGS": [
                            "-stdlib=libc++"
                        ],
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                        'GCC_ENABLE_CPP_RTTI': 'YES'
                    }
                }]
            ]
        }
    ]
}
