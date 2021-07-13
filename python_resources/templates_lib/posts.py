class Posts:

    data = dict(
        layout="posts",
        title="",
        date="",
        image="",
        tags=""
    )

    def template(self):
        return '\n'.join([
            '---',
            '\n'.join([name + ": " + self.data[name] for name in list(self.data)]),
            '---', '> <h3><strong>"TEXT".</strong></h3>'
        ])

    def cite(self, data):
        return '\n'.join([
                   '***\n', '> "{text}". — {author}. {cited_data}.', '***\n'
        ]).format(**data).ljust(0)