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
    path: '/puzzle',
    name: 'puzzle',
    component: () => import(/* webpackChunkName: "about" */ '../views/PuzzleView.vue')
  }, {
    path: '/blog',
    name: 'blog',
    component: () => import(/* webpackChunkName: "about" */ '../views/BlogView.vue')
  }, {
    path: '/suggestions',
    name: 'suggestions',
    component: () => import(/* webpackChunkName: "about" */ '../views/SuggestionsView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
