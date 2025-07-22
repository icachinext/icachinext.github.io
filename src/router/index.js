import Vue from 'vue'
import Router from 'vue-router'


const Home = () => import(/* webpackChunkName: "Home" */ '../components/Home.vue')
// const User = () => import(/* webpackChunkName: "User" */ '../components/User.vue')

const HomePage = () => import(/* webpackChunkName: "HomePage" */ '../components/home/HomePage.vue')
const ByLaws = () => import(/* webpackChunkName: "ByLaws" */ '../components/home/ByLaws.vue')
const AboutUs = () => import(/* webpackChunkName: "AboutUs" */ '../components/home/AboutUs.vue')
const NewsRoom = () => import(/* webpackChunkName: "NewsRoom" */ '../components/home/NewsRoom.vue')
const Conference = () => import(/* webpackChunkName: "Conference" */ '../components/home/Conference.vue')
const Resource = () => import(/* webpackChunkName: "Resource" */ '../components/home/Resource.vue')
const Contacts = () => import(/* webpackChunkName: "Contacts" */ '../components/home/Contacts.vue')
const NowNews = () => import(/* webpackChunkName: "NowNews" */ '../components/home/NowNews.vue')


const Post = () => import(/* webpackChunkName: "Post" */ '../components/home/Post.vue')

const SignIn = () => import(/* webpackChunkName: "SignIn" */ '../components/auth/SignIn.vue')
const SignUp = () => import(/* webpackChunkName: "SignUp" */ '../components/auth/SignUp.vue')
const Recover = () => import(/* webpackChunkName: "Recover" */ '../components/auth/Recover.vue')
const Verify = () => import(/* webpackChunkName: "Verify" */ '../components/auth/Verify.vue')
const Reset = () => import(/* webpackChunkName: "Reset" */ '../components/auth/Reset.vue')
const Paying = () => import(/* webpackChunkName: "Reset" */ '../components/home/Paying.vue')
const UserInfo = () => import(/* webpackChunkName: "UserInfo" */ '../components/auth/UserInfo.vue')


Vue.use(Router)

const routes = [
  {path :'/paying', component: Paying},
  // { path: '/', redirect: '/Home' },
  // { path: '/signin', component: Login },
  { path: '/',
    component: Home,
    // redirect: '/home',
    children: [
      { path: '', component: HomePage },
      { path: 'aboutus', component: AboutUs },
      { path: 'bylaws', component: ByLaws },
      { path: 'newsroom', component: NewsRoom },
      { path: 'conference', component: Conference },
      { path: 'resource', component: Resource },
      { path: 'contacts', component: Contacts },
      { path: 'post/:post_id', component: Post },
      { path: 'nownews', component:NowNews},
    ]

  },

  { path: '/auth',
    component: Home,
    redirect: '/auth/signin',
    children: [
      { path: 'signin', component: SignIn },
      { path: 'signup', component: SignUp },
      { path: 'recover', component: Recover },
      { path: 'verify', component: Verify },
      { path: 'reset', component: Reset },
      {path: 'UserInfo',component: UserInfo},
    ]
  }
]

const router = new Router({
  routes,
  // linkActiveClass: "active",
  linkExactActiveClass: 'active',
  mode: 'history'
})

export default router
