from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return ''


@app.route('/routes')
def routes():
    return jsonify([
        {
            'name': 'Route 1',

            'description': 'Praesent efficitur, sapien in elementum elementum, sem felis varius massa, vel aliquet mi dolor vel lacus. '
                           'Suspendisse tincidunt posuere ultrices. '
                           'In aliquam, mauris ut accumsan viverra, neque ex hendrerit ex, vitae hendrerit mi est nec enim. '
                           'Aliquam sem nunc, interdum sit amet tortor et, porttitor fringilla metus. Cras non nulla lorem. '
                           'Donec tristique, elit nec efficitur aliquet, ex lorem vulputate mauris, quis scelerisque nibh justo ut purus.',

            'image': 'https://gyb3jw.bn1303.livefilestore.com/y4m3utlmDhFKKhO_Mfykxeu4nvr9bgYlXjCbeXq-AZaEic_'
                     'PAHwGYLmGOi4Cp4-DHg4p_9e14CtuhhzGmFHbsEuoH2JW2fteJESBYhp2Mt-W1Jb2bweZhi6_'
                     'V2G72Q9RrnRFp4F8FS93AitLvR_NHjoRrNCsfPWwdNtsd7YVVT8kNWyYulZgni5AjUOCawJGk1IQrJqsTiYMKAh21SMQU72aw/'
                     'apofLnwyi74.jpg?psid=1',

            'city': 'Kaliningrad',
            'country': 'Russia',
            'state': 'Kaliningrad oblast',
            'distance': 4251,
            'time': '03:04:07',
            'places': [
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
                }]
        },
        {
            'name': 'Route 2',

            'description': 'In hac habitasse platea dictumst. Nullam ac neque non quam auctor iaculis. '
                           'Mauris feugiat euismod diam. Duis id libero at odio consequat accumsan nec non metus. Nulla facilisi. '
                           'Pellentesque tristique viverra convallis. Mauris aliquam, mauris feugiat interdum facilisis, '
                           'eros ante molestie nibh, quis bibendum est tortor eget urna. Vivamus ut tellus a massa ultrices varius. '
                           'Pellentesque ac consectetur sapien. Nunc sodales cursus accumsan. Donec mollis dictum ipsum, vitae consequat odio euismod nec. ',

            'image': 'https://tprgjq.bn1303.livefilestore.com/y4mupO5PGE1Pk25vKTfTUx2WU7nJTYl4IXjr-BfP2-'
                     '9L3HA179L6whk38Kp5U3dLV5MeEiKNPHozc0w8KAmOd5mNx7nbu7hm3oMe_3v5Dqt6u3ZMEzQwGJ4ePp263Fb5MT9YgStfer6Rvs2BP4zDFzt3m03i-'
                     'wqq6KtbXs4_0yn_dRJRT1kWSNMVVH_yCFH5QLBESwy9n_6bOeqJI9Jqixj4Q/mKZwWxh_nh0.jpg?psid=1',

            'city': 'Kaliningrad',
            'country': 'Russia',
            'state': 'Kaliningrad oblast',
            'distance': 4251,
            'time': '03:04:07',
            'places': [
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
                }]
        }
    ])


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
