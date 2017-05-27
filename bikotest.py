from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return ''


@app.route('/routes')
def routes():
    return ''


@app.route('/places')
def places():
    return jsonify([
        {
            'name': 'Place 1',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ac placerat nisi. '
                           'Praesent vitae lorem lectus. In nec viverra ipsum, eget eleifend purus. '
                           'Phasellus auctor sed est non accumsan.',
            'address': '',
            'lat': 54.7063551,
            'lng': 20.5120827,
            'city': 'Kaliningrad',
            'country': 'Russia',
            'state': 'Kaliningrad oblast'
        },
        {
            'name': 'Place 2',
            'description': 'Proin velit neque, rutrum id urna non, fringilla elementum lacus. '
                           'Fusce faucibus lacus nibh, eget scelerisque diam malesuada sed. '
                           'In tempor mi et erat ornare elementum.',
            'address': '',
            'lat': 54.6959517,
            'lng': 20.519152,
            'city': 'Saint Petersburg',
            'country': 'Russia',
            'state': 'Leningrad oblast'
        },
        {
            'name': 'Place 3',
            'description': 'Nunc lacinia, felis quis convallis volutpat, '
                           'nisl metus tincidunt elit, ut ornare sapien arcu ac lectus. '
                           'Vivamus quis elit sed tortor efficitur tristique ut non orci.',
            'address': '',
            'lat': 54.7204021,
            'lng': 20.5009085,
            'city': 'Vologda',
            'country': 'Russia',
            'state': 'Vologda oblast'
        },
        {
            'name': 'Place 4',
            'description': 'Nam risus ipsum, finibus vitae lobortis sodales, ultricies in ipsum. '
                           'Donec ultrices aliquet lectus, quis interdum libero auctor et. '
                           'Aliquam bibendum urna diam, nec viverra dolor pharetra et.',
            'address': '',
            'lat': 54.706577,
            'lng': 20.500301,
            'city': 'Petrozavodsk',
            'country': 'Russia',
            'state': 'Petrozavodsk oblast'
        },
        {
            'name': 'Place 5',
            'description': 'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. '
                           'Phasellus id dignissim augue.',
            'address': '',
            'lat': 54.6967558,
            'lng': 20.5018666,
            'city': 'Moscow',
            'country': 'Russia',
            'state': 'Moscow oblast'
        }
    ])

if __name__ == '__main__':
    app.run()
