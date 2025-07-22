<template>

</template>

<script>
import {get} from '../../../static/vendor/leaflet/src/dom/DomUtil'

export default {
  data () {
    return {
      payForm: {
        paymentId: '',
        PayerID:''
  }
  }

  },
  name: 'Paying',
  created () {
    var query = this.$route.query
    let paymentId = query.paymentId
    let PayerID = query.PayerID
    this.payForm.paymentId = paymentId
    this.payForm.PayerID = PayerID
    console.log(paymentId)
    this.get()
  },
  methods: {
    get () {
      this.$axios.post('/public/paypal/success', this.payForm)
        .then(res => {
          console.log(res.data)
          if (res.data.code === 200){
            alert('支付成功！')
            this.$router.push('/')
          }
        })
        .catch(err => {
          console.error(err)
        })
    }
  }
}
</script>

<style scoped>

</style>
