<template>
  <div class="modal fade" :id="modal_id" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
          <h4 class="modal-title" id="myModalLabel"></h4>
        </div>
        <div class="modal-body">{{modal_content}}</div>
        <div class="modal-footer">
          <!--            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>-->
          <button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button>
        </div>
      </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
  </div>

</template>

<script>
export default {
  props:{
    modal_content:String,
    modal_id:String,
  }
}
</script>


