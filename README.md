# Bro2Graph

## Prerequisites
Bro2Graph relies on a few third-party packages, namely the Rexster server (https://github.com/tinkerpop/rexster/wiki/Downloads) and the 'Bulbs' Python interface (http://bulbflow.com).  

### Installing & Configuring Rexster
Installation is the very simple.  Just download the latest version of the Rexster Server package from the above URL.  At the time of this writing, that would be v2.6.0.  It's all one big Zip file, so just extract it somewhere convenient.  

Once unzipped, you will need to edit the _config/rexster.xml_ file to create the database used by our scripts.  Find the beginning of the `<graphs>` stanza (where, obviously, all the graphs are defined) and insert the following:

	<graph>                                                                 
	 <graph-name>hunting</graph-name>
	 <graph-type>tinkergraph</graph-type>                                
	 <graph-mock-tx>true</graph-mock-tx>                                 
         <extensions>                                                        
             <allows>                                                        
                 <allow>tp:gremlin</allow>                                   
             </allows>                                                       
         </extensions>                                                       
    </graph>                                                                

### Installing Bulbs
Bulbs is available through PyPi, so you can install it quite easily:

	# pip install bulbs

## Starting the Graph Environment
When you begin your hunting session, the first thing you'll need to do is to start the graph database backend, like so:

	[...]/rexster-server-2.6.0> ./bin/rexster.sh --start
	
You'll get a lot of output, but after a few seconds, the database will be initialized and ready for action.

## Loading Bro Data Into the Graph

	[...]/Bro2Graph> ./db-load.py -l ~/BroLogDir
	

