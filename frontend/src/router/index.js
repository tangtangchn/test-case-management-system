import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/views/HomePage'
import UploadRecords from '@/views/UploadRecords'
import GenerateCases from '@/views/GenerateCases'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/upload',
      name: 'UploadRecords',
      component: UploadRecords
    },
    {
      path: '/generate',
      name: 'GenerateCases',
      component: GenerateCases
    }
  ],
  // 去除/#
  mode: 'history'
})
