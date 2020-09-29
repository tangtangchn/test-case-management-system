<template>
  <div>
    <el-popover
      ref="popover1"
      placement="bottom-start"
      width="160"
      trigger="hover"
      content="批量上传已勾选的记录单">
    </el-popover>
    <el-button
      class="uploadBtn"
      size="normal"
      type="primary"
      @click="submitUpload"
      :disabled="this.multipleSelection.length === 0"
      v-popover:popover1>
      上传记录单
    </el-button>
  </div>
</template>

<script>
import bus from '@/assets/eventBus'

export default {
  data () {
    return {
      // 兄弟组件【ImportTable】传来的值
      tableData3: [],
      multipleSelection: []
    }
  },
  methods: {
    submitUpload () {
      for (let i = 0; i < this.multipleSelection.length; i++) {
        let blobURL = this.multipleSelection[i].blob_url
        // 获取blob对象，并上传至后端
        fetch(blobURL, {
          method: 'get'
        })
          .then(response => response.blob())
          .then(blob => {
            let fd = new FormData()
            fd.append('fileData', blob, this.multipleSelection[i].modName)
            let headers = new Headers()
            headers.set('Access-Control-Allow-Origin', '*')
            headers.set('Access-Control-Allow-Methods', 'OPTIONS,HEAD,GET,POST')
            headers.set('contentType', 'application/form-data; charset=utf-8')
            this.$http({
              method: 'post',
              url: 'http://127.0.0.1:5000/api/files_from_frontend',
              data: fd,
              headers: headers
            })
              .then(function (res) {
                console.log(res)
              })
              .catch(function (error) {
                console.log(error)
              })
          })
          .then(res => console.log(res))
          .catch(error => console.log(error))
      }
      // 为兄弟组件【ImportTable】更新数据
      for (let i = 0; i < this.multipleSelection.length; i++) {
        for (let j = 0; j < this.tableData3.length; j++) {
          if (this.multipleSelection[i].id === this.tableData3[j].id) {
            this.tableData3[j].status = '已上传'
          }
        }
      }
      bus.$emit('modifyTableData', this.tableData3)
    }
  },
  mounted () {
    const self = this
    // 接受兄弟组件【ImportTable】传来的值
    bus.$on('changeSelection', function (data) {
      self.multipleSelection = data
    })
    bus.$on('tableData', function (data) {
      self.tableData3 = data
    })
  }
}
</script>
