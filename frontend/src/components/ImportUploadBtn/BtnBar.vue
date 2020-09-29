<template>
  <div class="btn-bar">
    <div class="btn-import">
      <importbtn></importbtn>
    </div>
    <div class="btn-remove">
      <removebtn></removebtn>
    </div>
    <div class="btn-upload">
      <uploadbtn></uploadbtn>
    </div>
  </div>
</template>

<script>
import ImportBtn from '@/components/ImportUploadBtn/components/ImportBtn'
import RemoveBtn from '@/components/ImportUploadBtn/components/RemoveBtn'
import UploadBtn from '@/components/ImportUploadBtn/components/UploadBtn'

export default {
  components: {
    'importbtn': ImportBtn,
    'removebtn': RemoveBtn,
    'uploadbtn': UploadBtn
  },
  data () {
    return {
      // pass
    }
  }
}
</script>

<style>
.btn-bar {
  float: left;
}
.btn-import {
  display: inline-block;
}
.btn-remove {
  display: inline-block;
}
.btn-upload {
  display: inline-block;
}
</style>
