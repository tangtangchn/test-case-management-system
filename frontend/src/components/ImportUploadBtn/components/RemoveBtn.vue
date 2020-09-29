<template>
  <div>
    <el-popover
      ref="popover1"
      placement="bottom-start"
      width="160"
      trigger="hover"
      content="批量移除已勾选的记录单">
    </el-popover>
    <el-button
      class="removeBtn"
      size="normal"
      type="danger"
      @click="deleteRows"
      :disabled="this.multipleSelection.length === 0"
      v-popover:popover1>
      移除记录单
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
    // 批量删除【ImportTable】表格中的行
    deleteRows: function () {
      if (this.multipleSelection.length > 0) {
        let notDelArray = []
        const len = this.tableData3.length
        for (let i = 0; i < len; i++) {
          if (this.multipleSelection.indexOf(this.tableData3[i]) >= 0) {
            console.log(this.multipleSelection.indexOf(i))
          } else {
            notDelArray.push(this.tableData3[i])
          }
        }
        this.tableData3 = notDelArray
        this.multipleSelection = []
        // 为兄弟组件【ImportTable】更新数据
        bus.$emit('updateTableData', this.tableData3)
        bus.$emit('updateSelection', this.multipleSelection)
      }
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
