// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// 【饿了么】的【组件库】
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// Vue本身不支持发送Ajax请求
// 安装axios插件用于http请求
import axios from 'axios'

Vue.use(ElementUI)
// 能够直接在组件的methods中使用$http命令
Vue.prototype.$http = axios

// 全局注册组件
// 建议采用局部注册组件
// import TopBar from '@/components/TopBar'
// Vue.component('topbar', TopBar)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
