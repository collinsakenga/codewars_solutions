import java.util.List;

// TODO: complete this object/class

public class PaginationHelper<I> {

  private List<I> list;
  private int num;
  public PaginationHelper(List<I> collection, int itemsPerPage) {
    this.list=collection;
    this.num=itemsPerPage;
  }
  
  /**
   * returns the number of items within the entire collection
   */
  public int itemCount() {
    return this.list.size();
  }
  
  /**
   * returns the number of pages
   */
  public int pageCount() {
    if (this.list.isEmpty()) {
      return 0;
    }
    int count=this.list.size()/this.num;
    if (this.list.size()%this.num!=0) {
      count+=1;
    }
    return count;
  }
  
  /**
   * returns the number of items on the current page. page_index is zero based.
   * this method should return -1 for pageIndex values that are out of range
   */
  public int pageItemCount(int pageIndex) {
    if (pageIndex>=pageCount() || pageIndex <0) {
      return -1;
    }
    if (itemCount()/((pageIndex+1)*this.num)!=0) {
      return this.num;
    }
    return itemCount()%this.num;
  }
  
  /**
   * determines what page an item is on. Zero based indexes
   * this method should return -1 for itemIndex values that are out of range
   */
  public int pageIndex(int itemIndex) {
    if (itemIndex<0 || itemIndex>itemCount() || pageCount()==0) {
      return -1;
    }
    return itemIndex/this.num;
  }  
}