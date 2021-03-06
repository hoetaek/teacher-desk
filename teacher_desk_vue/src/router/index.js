import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/worksheet',
    name: 'worksheet',
    component: () => import(/* webpackChunkName: "about" */ '../views/WorksheetView.vue')
  }, {
    path: '/wordsearch',
    name: 'wordsearch',
    component: () => import(/* webpackChunkName: "about" */ '../views/WordsearchView.vue')
  }, {
    path: '/wordsearch/en',
    name: 'english_wordsearch',
    component: () => import(/* webpackChunkName: "about" */ '../views/WordsearchEnglishView.vue')
  }, {
    path: '/wordsearch/kr',
    name: 'korean_wordsearch',
    component: () => import(/* webpackChunkName: "about" */ '../views/WordsearchKoreanView.vue')
  }, {
    path: '/suggestion',
    name: 'suggestion',
    component: () => import(/* webpackChunkName: "about" */ '../views/SuggestionView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
