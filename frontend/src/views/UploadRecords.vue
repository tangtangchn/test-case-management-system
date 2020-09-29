<template>
  <div class="container">
    <div class="nav">
      <topbar></topbar>
    </div>
    <div class="main">
      <div class="selections">
        <namerules></namerules>
      </div>
      <div class="operations">
        <btnbar></btnbar>
        <importtable></importtable>
      </div>
    </div>
    <div class="footer">
      <pagefooter></pagefooter>
    </div>
  </div>
</template>

<script>
import TopBar from '@/components/TopBar'
import NamingRules from '@/components/SelectRules/NamingRules'
import BtnBar from '@/components/ImportUploadBtn/BtnBar'
import ImportTable from '@/components/ImportTable'
import PageFooter from '@/components/PageFooter'

export default {
  name: 'Upload',
  components: {
    'topbar': TopBar,
    'namerules': NamingRules,
    'btnbar': BtnBar,
    'importtable': ImportTable,
    'pagefooter': PageFooter
  },
  data () {
    return {
      // pass
    }
  }
}
</script>

<style scoped>
.container {
  position: absolute;
  width: 100%;
  min-width: 1024px;
  min-height: 100%;
  left: 0;
  right: 0;
  top: 0;
}
.main {
  margin-top: 100px;
  padding-bottom: 50px;
}
.selections {
  float: left;
  margin-left: 300px;
  display: inline-block;
}
.operations {
  float: left;
  margin-left: 20px;
  padding-top: 15px;
  padding-left: 15px;
  display: inline-block;
  width: 980px;
  border: 1px solid #EFF2F7;
  background-color: #F9FAFC;
}
</style>
