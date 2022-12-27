# toobuk_vued3
python을 공부하면서 간단한 모듈을 만들었습니다.  
https://github.com/ramoi/toobuk  
그러다 좀 욕심이 생겨서 화면도 만들었네요  
https://github.com/ramoi/vue-d3  

그래서 두 놈을 연동해보았습니다.  
아마도 실무에서는 쓰지 않을테지요  
웹크롤링을 하는 더 좋은 라이브러리가 있을테구요  
vue-d3는 기능이 미미합니다. 실무에서는 쓸 수 없어요  
다만 이제 시작하는 분들에게 도움이 된다면 좋을 것 같네요  

아래에서 그 내용을 확인할 수 있습니다.  
https://toobuk.herokuapp.com

## 차례
1. [설치](#설치)
1. [django 실행](#django-실행)
1. [vue-연동](#vue-연동)

### 설치 
python을 설치했다는 가정하에 진행합니다. 아래 사이트를 참고해주세요  
https://wikidocs.net/8

    pip install django
    pip install beautifulsoup4 toobuk
    pip install whitenoise gunicor



그리고 작업 디렉토리를 만드 후, github에서 소스를 받아옵니다.

    mkdir project
    cd project
    git init
    git clone https://github.com/ramoi/toobuk_vued3.git

toobuk_vued3/statist/settings.py 수정

주석처리  
46라인

    'whitenoise.middleware.WhiteNoiseMiddleware',
    ->
    'whitenoise.middleware.WhiteNoiseMiddleware',

128라인

    STATIC_ROOT = os.path.join(BASE_DIR, 'templates/static')  
    ->
    STATIC_ROOT = os.path.join(BASE_DIR, 'templates/static')  

### django 실행
django 디렉토리로 이동해서 서버를 실행시킵니다.
    
    cd project/toobuk_vued3
    python manage.py runserver
    http://localhost:8000/

### vue 연동
vue 연동은 안하셔도 됩니다. 다만, vuejs를 수정하면서 화면을 보고 싶다면 아래 참고하시면 됩니다.  
완전한 연동은 아니고, vuejs에서 build를 하여 django의 static디렉토리에 build.js를 떨어뜨리는 방식입니다.  

만일 작업 디렉토리가 C:\project 그 하위에 statist라는 디렉토리가 생성이 되었을겁니다.  
C:\project 하위에 vue 라는 디렉토리를 만듭니다.  
이제 vue 디렉토리가 vue 작업 디렉토리입니다.  
https://github.com/ramoi/vue-d3#%EC%84%A4%EC%B9%98 로 가셔서 해당 프로젝트를 설치합니다.  
정상적으로 설치하시면 webpack.config.js 파일이 생성될텐데요. 해당 파일을 수정합니다.  

~~~
var path = require('path')

var vs = {
  entry: './src/mainChart.js',
  output: {
    path: path.resolve(__dirname, './static'),
    publicPath: '/static/',
    filename: 'build.js'
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ],
      },      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      }
    ]
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    },
    extensions: ['*', '.js', '.vue', '.json']
  },
  devServer: {
    historyApiFallback: true,
    noInfo: true,
    overlay: true
  },
  performance: {
    hints: false
  },
  devtool: '#eval-source-map'
}

var ds = {}
for( var e in vs) {
  ds[e] = vs[e]
}

ds.entry = './src/main.js'
ds.output = {
    path: path.resolve(__dirname, '../../statist/templates/static'),
    publicPath: '/static/',
    filename: 'build.js'
}

module.exports = [
  vs, ds
]

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}
~~~

vue 디렉토리로 이동해서 빌드!!  

	cd vue\chart
	yarn run build

