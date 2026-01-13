import DefaultTheme from 'vitepress/theme'
import './style.css'
import HeroSlide from '../../../components/HeroSlide.vue'
import BoardMembers from '../../../components/BoardMembers.vue'
import NewsList from '../../../components/NewsList.vue'
import ConferenceGrid from '../../../components/ConferenceGrid.vue'

export default {
    extends: DefaultTheme,
    enhanceApp({ app }) {
        app.component('HeroSlide', HeroSlide)
        app.component('BoardMembers', BoardMembers)
        app.component('NewsList', NewsList)
        app.component('ConferenceGrid', ConferenceGrid)
    }
}
