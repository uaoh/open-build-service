class AddPackageColumnToFlagsTable < ActiveRecord::Migration[5.1]
  def change
    add_column :flags, :pkgname, :string, :limit => 255, :null => true
  end
end
