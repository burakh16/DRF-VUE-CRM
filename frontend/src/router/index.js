import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/products',
    name: 'ProductList',
    component: () => import( '../views/ProductList.vue')
  },
  {
    path: '/product',
    name: 'Product',
    component: () => import( '../views/Product.vue'),
    children: [
      { path: ':id', component: () => import( '../views/Product.vue')}
    ]
  },
  {
    path: '/customers',
    name: 'CustomerList',
    component: () => import( '../views/CustomerList.vue')
  },
  {
    path: '/customer',
    name: 'Customer',
    component: () => import( '../views/Customer.vue'),
    children: [
      { path: ':id', component: () => import( '../views/Customer.vue')}
    ]
  },
  {
    path: '/orders',
    name: 'OrderList',
    component: () => import( '../views/OrderList.vue')
  },
  {
    path: '/order',
    name: 'order',
    component: () => import( '../views/Order.vue'),
    children: [
      { path: ':id', component: () => import( '../views/Order.vue')}
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
