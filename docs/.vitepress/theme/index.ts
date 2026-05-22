import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import './style.css'

import Layout from './Layout.vue'

import BoardMembers from '../../../components/BoardMembers.vue'
import NewsList from '../../../components/NewsList.vue'
import ConferenceGrid from '../../../components/ConferenceGrid.vue'
import ResourceList from '../../../components/ResourceList.vue'
import HomeHero from '../../../components/HomeHero.vue'
import HomeAbout from '../../../components/HomeAbout.vue'
import HomeConferences from '../../../components/HomeConferences.vue'
import HomeNewsAndResources from '../../../components/HomeNewsAndResources.vue'

const theme: Theme = {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app }) {
    app.component('BoardMembers', BoardMembers)
    app.component('NewsList', NewsList)
    app.component('ConferenceGrid', ConferenceGrid)
    app.component('ResourceList', ResourceList)
    app.component('HomeHero', HomeHero)
    app.component('HomeAbout', HomeAbout)
    app.component('HomeConferences', HomeConferences)
    app.component('HomeNewsAndResources', HomeNewsAndResources)
  }
}

export default theme
