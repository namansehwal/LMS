import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'

import LibrarianDashboard from '../views/librarian/LibrarianDashboard.vue'
import LibrarianSections from '../views/librarian/LibrarianSections.vue'
import LibrarianBooks from '../views/librarian/LibrarianBooks.vue'
import LibrarianRequests from '../views/librarian/LibrarianRequests.vue'
import LibrarianAccessLogs from '../views/librarian/LibrarianAccessLogs.vue'


import UserDashboard from '../views/user/UserDashboard.vue'
import UserBooks from '../views/user/UserBooks.vue'
import UserProfile from '../views/user/UserProfile.vue'
import UserSpace from '../views/user/UserSpace.vue'
import UserRequests from '../views/user/UserRequests.vue'

const routes = [
  {
    path: '/',
    alias: '/login',
    name: 'Login',
    component: Login,
    meta: {
      requireLogin: false
    }
  },
  {
    path: '/librarian',
    name: 'Librarian',
    component: LibrarianDashboard,
    meta: {
      requireLogin: true,
      role: 'librarian'
    },
    children: [
      {
        path: '',
        name: 'LibrarianDashboard',
        component: LibrarianDashboard
      },
      {
        path: 'dashboard',
        name: 'LibrarianDashboard',
        component: LibrarianDashboard
      },
      {
        path: 'sections',
        name: 'LibrarianSections',
        component: LibrarianSections
      },
      {
        path: 'books',
        name: 'LibrarianBooks',
        component: LibrarianBooks
      },
      {
        path: 'requests',
        name: 'LibrarianRequests',
        component: LibrarianRequests
      },
      {
        path: 'accesslogs',
        name: 'LibrarianAccessLogs',
        component: LibrarianAccessLogs
      }
    ]
  },
  {
    path: '/user',
    name: 'User',
    component: UserDashboard,
    meta: {
      requireLogin: true,
      role: 'user'
    },
    children: [
      {
        path: '',
        name: 'UserDashboard',
        component: UserDashboard
      },
      {
        path: 'dashboard',
        name: 'UserDashboard',
        component: UserDashboard
      },
      {
        path: 'books',
        name: 'UserBooks',
        component: UserBooks
      },
      {
        path: 'requests',
        name: 'UserRequests',
        component: UserRequests
      },
      {
        path: 'profile',
        name: 'UserProfile',
        component: UserProfile
      },
      {
        path: 'space',
        name: 'UserSpace',
        component: UserSpace
      }
    ]
  },
  {
    path: '/logout',
    name: 'Logout',
    beforeEnter: (to, from, next) => {
      localStorage.clear()
      next('/login')
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  // Check if the route requires authentication
  if (to.meta.requireLogin) {
    const token = localStorage.getItem('access_token')
    const role = localStorage.getItem('role')
    const now = new Date()

    if (to.meta.role === role) {
      next()
    } else {
      localStorage.clear()
      next('/login')
    }
  } else {
    next()
  }
})

export default router
