import java.io.IOException;
import java.util.Iterator;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
public class WordCount {
//Mapper class
public static class WordMapper extends Mapper<Object, Text, Text, IntWritable> {
 private Text word = new Text();
 private final static IntWritable one = new IntWritable(1);
  
 @Override
 public void map(Object key, Text value,
   Context contex) throws IOException, InterruptedException {
StringTokenizer wordList = new StringTokenizer(value.toString());
       while (wordList.hasMoreTokens()) {
          word.set(wordList.nextToken());
             contex.write(word, one);
               }
            }
       }
//Reducer class
public static class SumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
  
 private IntWritable totalWordCount = new IntWritable();
  
 @Override
 public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
int wordCount = 0;
  Iterator<IntWritable> it=values.iterator();
  while (it.hasNext()) {
   wordCount += it.next().get();
  }
  totalWordCount.set(wordCount);
  context.write(key, totalWordCount);
 }
}
 


