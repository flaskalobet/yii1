<?php

class m150624_034228_tasks extends CDbMigration
{
	public function up()
	{
        $this->createTable('tasks', array(
           'id' => 'INTEGER PRIMARY KEY',
           'title' => 'TEXT',
           'data' => 'TEXT',
           'project_id' => 'INTEGER',
           'completed' => 'INTEGER',
           'due_date' => 'INTEGER',
           'created' => 'INTEGER',
           'updated' => 'INTEGER'
        ));
        $this->createTable('projects', array(
           'id' => 'INTEGER PRIMARY KEY',
           'name' => 'TEXT',
           'completed' => 'INTEGER',
           'due_date' => 'INTEGER',
           'created' => 'INTEGER',
           'updated' => 'INTEGER'
        ));
	}

	public function down()
	{
		//echo "m150624_034228_tasks does not support migration down.\n";
		//return false;
        $this->dropTable('projects');
        $this->dropTable('tasks');
	}

	/*
	// Use safeUp/safeDown to do migration with transaction
	public function safeUp()
	{
	}

	public function safeDown()
	{
	}
	*/
}
