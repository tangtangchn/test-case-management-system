<template>
  <div>
    <div class="cancelBtn">
      <el-button
        :plain="true"
        type="warning"
        size="small"
        @click="toggleSelection()"
        :disabled="this.multipleSelection.length === 0">
        取消勾选
      </el-button>
    </div>
    <div class="import-table">
      <el-table
        ref="multipleTable"
        :data="tableData3"
        border
        tooltip-effect="dark"
        style="width: 966px;overflow: auto"
        :header-cell-style="tableHeaderStyle"
        :cell-style="tableCellStyle"
        @selection-change="handleSelectionChange">
        <el-table-column header-align="center"
          type="index"
          label="序号"
          width="62">
        </el-table-column>
        <el-table-column header-align="center"
          prop="product"
          label="产品编号"
          width="158"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column header-align="center"
          prop="name"
          label="记录单"
          width="350"
          show-overflow-tooltip>
        </el-table-column>
        <!-- 此项不展示给用户
        <el-table-column header-align="center" id="col-mod-name"
          prop="modName"
          label="按命名规则维护后的记录单名称"
          show-overflow-tooltip>
        </el-table-column>
        -->
        <el-table-column header-align="center"
          prop="size"
          label="文件大小"
          width="82">
        </el-table-column>
        <el-table-column header-align="center"
          label="操作"
          width="155">
          <template slot-scope="scope">
            <el-button
              @click.native.prevent="deleteRow(scope.$index, tableData3)"
              type="danger"
              size="mini">
              移 除
            </el-button>
            <el-button
              @click.native.prevent="uploadRow(scope.$index, tableData3)"
              type="primary"
              size="mini">
              上 传
            </el-button>
          </template>
        </el-table-column>
        <el-table-column header-align="center"
          prop="status"
          label="状态"
          width="80">
        </el-table-column>
        <el-table-column header-align="center"
          type="selection"
          width="78"
          :selectable="isSelectable">
        </el-table-column>
        </el-table>
    </div>
    <ol>
      <li v-for="file in importedFiles" :key="file.string">
        {{ file }}
      </li>
    </ol>
    <ol>
      <li v-for="file in tableData3" :key="file.string">
        {{ file }}
      </li>
    </ol>
    <ol>
      <li v-for="select in multipleSelection" :key="select.string">
        {{ select }}
      </li>
    </ol>
  </div>
</template>

<script>
import bus from '@/assets/eventBus'

export default {
  data () {
    return {
      // 兄弟组件【ImportBtn】传来的值
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
      pf: '',
      // 动态数据
      tableData3: [],
      multipleSelection: []
    }
  },
  methods: {
    toggleSelection (rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    handleSelectionChange (val) {
      this.multipleSelection = val
      // 向兄弟组件【RemoveBtn】传值
      bus.$emit('changeSelection', this.multipleSelection)
      bus.$emit('tableData', this.tableData3)
    },
    deleteRow (index, rows) {
      rows.splice(index, 1)
      // 为兄弟组件【ImportBtn】更新数据
      this.importedFiles = this.tableData3
      bus.$emit('updateFileList', this.importedFiles)
    },
    uploadRow (index, rows) {
      // pass
    },
    isSelectable (row) {
      if (row.status === '已上传') {
        // 若状态变为“已上传”，当前行checkbox禁用
        return 0
      } else {
        return 1
      }
    },
    unChecked (rows) {
      rows.forEach(row => {
        if (row.status === '已上传') {
          // 当状态变为“已上传”时，取消当前行checkbox的勾选
          this.$refs.multipleTable.toggleRowSelection(row, false)
        }
      })
    },
    tableHeaderStyle ({row, column, rowIndex, columnIndex}) {
      return 'backgroundColor:#F9FAFC'
    },
    tableCellStyle ({row, column, rowIndex, columnIndex}) {
      if (row.status === '已上传') {
        return 'backgroundColor:#E0EEE0'
      }
    }
  },
  mounted () {
    const self = this
    // 接受兄弟组件【ImportBtn】传来的值
    bus.$on('shareFileList', function (data) {
      self.importedFiles = data
      // 动态加载表格数据
      const dataForTable = []
      for (let k = 0; k < self.importedFiles.length; k++) {
        const obj = {}
        obj.id = self.importedFiles[k].uid
        obj.product = self.product
        obj.name = self.importedFiles[k].name
        // 分割文件名与后缀名
        let tempName = obj.name.substring(0, obj.name.lastIndexOf('.'))
        let tempExtension = obj.name.substring(obj.name.lastIndexOf('.') + 1)
        // 拼接按命名规则维护后的记录单文件名
        obj.modName = self.batch + '-' + self.testType + '-' + self.round + '-' +
          tempName + '_' + self.pf + '.' + tempExtension
        // 计算文件大小，显示【KB】或【MB】
        let fileSize = self.importedFiles[k].size
        if (fileSize < 1048576) {
          obj.size = (fileSize / 1024).toFixed(1) + 'KB'
        } else if (fileSize >= 1048576) {
          obj.size = (fileSize / (1024 * 1024)).toFixed(1) + 'MB'
        } else {
          obj.size = fileSize
        }
        // blob url
        obj.blob_url = self.importedFiles[k].url
        // 修改记录单状态为【待上传】
        // obj.status = self.importedFiles[k].status
        obj.status = '待上传'
        dataForTable[k] = obj
      }
      self.tableData3 = dataForTable
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
    // 接受兄弟组件【RemoveBtn】传来的更新
    bus.$on('updateTableData', function (data) {
      self.tableData3 = data
      // 为兄弟组件【ImportBtn】更新数据
      self.importedFiles = self.tableData3
      bus.$emit('updateFileList', self.importedFiles)
    })
    bus.$on('updateSelection', function (data) {
      self.multipleSelection = data
    })
    // 接受兄弟组件【UploadBtn】传来的更新
    bus.$on('modifyTableData', function (data) {
      self.tableData3 = data
      // 当状态变为“已上传”时，取消当前行checkbox的勾选
      // 延迟执行，在执行代码前等待3000毫秒
      setTimeout(function () {
        self.unChecked(self.tableData3)
      }, 3000)
    })
  }
}
</script>

<style>
.import-table {
  margin-top: 10px;
}
.cancelBtn {
  float: right;
  margin-right: 14px;
  margin-bottom: 5px;
}
</style>
