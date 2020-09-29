<template>
  <div>
    <el-popover
      ref="popover1"
      placement="bottom-start"
      width="200"
      trigger="hover"
      content="批量导入Word/Excel/PDF/压缩文件，压缩文件会在导入过程中自动解压">
    </el-popover>
    <el-upload
      class="import_files"
      action="https://XXX XXX XXX"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :file-list="importedFiles"
      :on-change="updateFileList"
      :auto-upload="false"
      :show-file-list="false"
      accept=".docx,.doc,.xlsx,.xls,.pdf,.zip,.rar,.7z,.tar"
      multiple>
      <el-button
        class="importBtn"
        size="normal"
        type="success"
        v-popover:popover1
        :disabled="this.product==='' || this.batch==='' || this.testType==='' || this.round==='' || this.pf===''">
        导入记录单
      </el-button>
    </el-upload>
  </div>
</template>

<script>
import bus from '@/assets/eventBus'

export default {
  data () {
    return {
      importedFiles: [],
      // 兄弟组件【SelectProduct】传来的值
      product: '',
      // 兄弟组件【SelectBatch】传来的值
      batch: '',
      // 兄弟组件【SelectTestType】传来的值
      testType: '',
      // 兄弟组件【SelectRoundID】传来的值
      round: '',
      // 兄弟组件【SelectPF】传来的值
      pf: ''
    }
  },
  methods: {
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    updateFileList: function (file, fileList) {
      this.importedFiles = fileList
      // 向兄弟组件【ImportTable】传值
      bus.$emit('shareFileList', this.importedFiles)
    }
  },
  mounted () {
    const self = this
    // 接受兄弟组件【ImportTable】传来的更新
    bus.$on('updateFileList', function (data) {
      self.importedFiles = data
    })
    // 接受兄弟组件【SelectProduct】传来的值
    bus.$on('newProduct', function (data) {
      self.product = data
    })
    // 接受兄弟组件【SelectBatch】传来的值
    bus.$on('newBatch', function (data) {
      self.batch = data
    })
    // 接受兄弟组件【SelectTestType】传来的值
    bus.$on('newTestType', function (data) {
      self.testType = data
    })
    // 接受兄弟组件【SelectRoundID】传来的值
    bus.$on('newRound', function (data) {
      self.round = data
    })
    // 接受兄弟组件【SelectPF】传来的值
    bus.$on('newPF', function (data) {
      self.pf = data
    })
  }
}
</script>
