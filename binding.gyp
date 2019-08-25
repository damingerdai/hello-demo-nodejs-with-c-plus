{
    'targets': [
        {
            'target_name': 'hello',
            'sources': [
                'src/hello.cc'
            ],
            'conditions': [
                [ 'OS == "win"', {
                    'libraries': [ '-Inode.lIB']
                }]
            ]
        }
    ]
}